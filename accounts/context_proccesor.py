from .forms import LoginForm, SignupForm




def login(request):
    Login_form = LoginForm()
    return {"Login_form":Login_form}



def signup(request):
    signup_form = SignupForm()
    return {"Signup_form":signup_form}