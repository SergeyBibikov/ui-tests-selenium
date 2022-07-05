def get_element_style_property(driver, css_selector, property_name):
    sc = f"return document.defaultView.getComputedStyle(document.querySelector('{css_selector}')).{property_name}"
    return driver.execute_script(sc)