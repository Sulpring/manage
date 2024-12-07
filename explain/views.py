from django.shortcuts import render
from django.http import JsonResponse
from asyncio import create_task, gather
import httpx
from manage_main.models import Product
from django.db.models import Case, When

# 이미지를 받아 찾고, 이를 기반으로 ai결과를 만들고 다시 프런트로 돌려주기
async def process_explain(request):
    if request.method == "POST":
        # 요청 받기
        imgs = request.POST.get("imgs")
        
        # 이거 기반으로 인공지능 쪽에 요청보내기
        ai_server_tasks = []
        for img in imgs:    
            ai_server_req = {
                "message": "이 이미지에 대해 설명해주세요",
                "file": img.img_file
            }
            url = "http://18.211.4.201:8000/analyze"
            ai_server_tasks.append(create_task(fetch_data(url, ai_server_req)))

        # db에서 찾기
        urls = []
        for img in imgs:
            urls.append(img.img_url)
        # DB에서 필터링된 QuerySet 가져오기
        preserved_order = Case(
            *[When(img_url=url, then=pos) for pos, url in enumerate(urls)]
        )
        queryset = Product.objects.filter(img_url__in=urls).order_by(preserved_order)

        # 각 URL에 대해 객체가 있는지 확인
        human_explain = [
            queryset.filter(img_url=url).first() or False  # 객체가 없으면 False 반환
            for url in urls
        ]
        # 요청 결과 받기
        ai_explain = await gather(*ai_server_req)

        explain_list = []
        for i in len(ai_explain):
            elem = {
                'img_url': urls[i],
                'human_explain': human_explain[i],
                'ai_explain': ai_explain[i]
            }
            explain_list.append(elem)

        response = {
            'explain_list': explain_list
        }

        return JsonResponse(data=response)
        
 

# 요청보내기
async def fetch_data(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.data(url, data)
        return response.json