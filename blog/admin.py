from django.contrib import admin

# Register your models here.
from blog import models

admin.site.site_header = 'ZLZ后台管理'
admin.site.site_title = 'ZLZ'

admin.site.register(models.User)
admin.site.register(models.ConfirmString)
admin.site.register(models.Article)
admin.site.register(models.Article2Category)
admin.site.register(models.Category)

# @admin.register(models.UserInfo)
# class UserInfoAdmin(admin.ModelAdmin):
#     # 设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('pk', 'username', 'sex', 'birthday', 'email', 'telephone', 'is_staff', 'is_active', 'date_joined')
#
#     # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
#     actions_on_top = True
#     # actions_on_bottom = True
#     # 操作项功能显示选中项的数目
#     actions_selection_counter = True
#     # 字段为空值显示的内容
#     empty_value_display = ' -空白- '
#
#     # list_editable 设置默认可编辑字段（name默认不可编辑，因为它是一个链接，点击会进入修改页面）
#     list_editable = ['sex', 'birthday', 'email', 'telephone', ]
#
#
# admin.site.register(models.Article)
# admin.site.register(models.Article2Category)
# admin.site.register(models.Category)
