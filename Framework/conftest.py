import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge", help="browser selection"
    )


@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver
    browser_name = request.config.getoption( "browser_name" )
    service_obj = Service()
    
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        
         
        driver = webdriver.Chrome(service=service_obj,options=chrome_options)
        
    elif browser_name == "firefox":
        driver = webdriver.Firefox( service=service_obj )
        
    elif browser_name == "edge":
        edge_options = EdgeOptions()
        
        edge_options.add_argument("--headless=new")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=service_obj,options=edge_options)
        
    print("Browser =", browser_name)
    print("Driver =", driver)
    print("Fixture Driver ID =", id(driver))
    
    driver.implicitly_wait( 5 )
    driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    yield driver  #Before test function execution
    driver.quit()  #post your test function execution


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call':
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join(reports_dir, "screen.png")
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    global driver   
    print("Driver =", driver)

    if driver is None:
        print("Driver is None")
        return

    print("Saving to =", file_name)
    result = driver.get_screenshot_as_file(file_name)
    print("Result =", result)
    print("Screenshot Driver ID =", id(driver))
