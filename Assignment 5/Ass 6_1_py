class Password_manager:
    def __init__(self):
        self.old_passwords=[]
    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None
    def set_password(self,new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
    def is_correct(self,password):
        return password==self.get_password()
pm=Password_manager()
pm.set_password('pass123')
print(pm.get_password())
print(pm.is_correct('pass123'))
pm.set_password('pavan675')
print(pm.get_password())
print(pm.is_correct('pavan3546'))
        
