class ModelFormMixin(ModelForm):
    def __init__(self,*args,**kwargs): #If user is passed as a keyword i.e 'user' here
        self.user = kwargs.pop('user')
        super(ModelFormMixin, self).__init__(*args, **kwargs)
        
    def __init__(self,user,*args,**kwargs):     #If user is passed as a positional argument (user = request.user)
        self.user = user
        super(ModelFormMixin, self).__init__(*args, **kwargs)
      
    def is_valid(self):
        self.instance.posted_by = self.user
        return super(ModelFormMixin,self).is_valid()
