from helloworld import say_hello

def test_helloworld_no_params():
    assert say_hello() == "Hello, World!. You have successfully downloaded first PyPi library created by your friend. Now, don't feel shy to donate using GPay/Paytm or whatever suits you!"

def test_helloworld_with_params():
    assert say_hello("XYZ") == "Hello, XYZ. You have successfully downloaded first PyPi library created by your friend. Now, don't feel shy to donate using GPay/Paytm or whatever suits you!"
