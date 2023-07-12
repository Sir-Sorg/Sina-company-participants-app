from fastapi import FastAPI
from routes.route import router

app = FastAPI()
app.include_router(router)

# TODO:
# ابتدا با استفاده از فریم ورک fastapi و دیتابیس mongodb یک template درست میکنید که صرفا چند route ساده دارد و authorize کاربر را انجام می دهد و میتوان به راحتی در آن route ایجاد کرد و بک اند یک سایت را با آن توسعه داد.
# یک route در آن مینویسید که با استفاده از کتابخانه requests داخل توییتر لاگین انجام شود و credentials اکانت در قالب json برگردانده شود.(از selenium استفاده نکنید) سپس این credentials را در دیتابیس ذخیره کنید. اگر اکانت مشکل داشت ارور 400 برگردانید و در غیر اینصورت آی دی داکیومنتی که در دیتابیس سیو شده را برگردانید.
# یک route اضافه کنید که با دریافت یک یوزرنیم و آی دی اکانتی که در دیتابیس ذخیره شده شده فالوور های آن یوزرنیم را استخراج کند و پس از تمیز کردن دیتا response را در غالب یک json برگردانید.
# نکات مهم:
# حتما تمامی مراحل را در git شخصی خود به مرور commit کنید و لینک ریپو آن را همینجا برای بنده ارسال کنید.
# برای Authorize از داکیومنت رسمی خود fastapi استفاده کنید.
# فرصت انجام این تسک تا پنج شنبه شب می باشد.
# هر جا سوال یا ابهامی بود بنده درخدمتم 🌹
