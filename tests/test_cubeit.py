import pytest
from playwright.sync_api import expect, sync_playwright, Page

BASE_URL = "http://uitestingplayground.com/sampleapp"

def test_valid_login(page: Page):
    page.goto(BASE_URL)
    
    input_user = page.get_by_placeholder("User Name")
    input_password = page.get_by_placeholder("********")
    input_user.fill("jbond")
    input_password.fill("pwd")
    
    btn_login = page.get_by_role("button", name="Log In")
    btn_login.click()

    label_status = page.locator("css=label#loginstatus")
    expect(label_status).to_have_text("Welcome, jbond!")

def test_invalid_login(page: Page):
    page.goto(BASE_URL)
    
    input_user = page.get_by_placeholder("User Name")
    input_password = page.get_by_placeholder("********")
    input_user.fill("jbond")
    input_password.fill("007")
    
    btn_login = page.get_by_role("button", name="Log In")
    btn_login.click()

    label_status = page.locator("css=label#loginstatus")
    expect(label_status).to_have_text("Invalid username/password")