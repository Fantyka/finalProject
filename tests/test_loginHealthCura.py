import pytest
from pages.login import Login
from pages.appointment import Appointment


def test_loginValid (setup):
    login = Login(setup)
    appointment = Appointment(setup)
    

    login.input_username('John Doe')
    login.input_password('ThisIsNotAPassword')
    login.klik_login()
    
    
    curl_url = setup.current_url
    assert curl_url == 'https://katalon-demo-cura.herokuapp.com/#appointment'

    appointment.cek_judulMakeAppointment()


data_login = [
             {'John Doe', 'bintang', 'Login failed! Please ensure the username and password are valid.'},
             {'karisma', 'ThisIsNotAPassword', 'Login failed! Please ensure the username and password are valid.'}
             ]

@pytest.mark.parametrize('username, password, error', data_login)
def test_loginInvalid (username, password, error, setup):
    login = Login(setup)
    
    login.input_username(username)
    login.input_password(password)
    login.klik_login()

    error_message = login.check_error_message()

    assert error_message == error

    
    
    
    




