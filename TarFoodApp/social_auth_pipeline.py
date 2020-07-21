from TarFoodApp.models import Customer,Driver


def create_user_by_type(backend,user,response,*args,**kwargs):
    if backend.name == 'facebook':
        avatar = 'http://graph.facebook.com/%s/picture?type=large' % response ['id']
    if request['user_type'] == "driver" and not Driver.objects.filter(user_id = user.id):
        Driver.objects.create(user_id=user.id,avatar=avatar)



