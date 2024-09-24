def test_user_new_address(user_driver):
    user_driver.get(userAddressPage.url)
    
    page = userAddressPage(user_driver)
    page = page.new_address()
    page_msg = page.submit(name,phone,province)
    
    
    assert page_msg = "操作成功"