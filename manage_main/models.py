from django.db import models

class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # 사용자 ID
    password = models.CharField(max_length=255)  # 비밀번호

    def __str__(self):
        return self.id


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")  # User와의 관계
    name = models.CharField(max_length=255)  # 상품 이름
    code = models.BigIntegerField()  # 상품 코드
    img_url = models.URLField(max_length=200, blank=True, null=True)  # 이미지 URL
    human_text = models.CharField(max_length=255, blank=True, null=True)  # 사람이 작성한 텍스트
    ai_text = models.JSONField(blank=True, null=True)  # AI가 생성한 텍스트 (JSON 형식)

    def __str__(self):
        return self.name
