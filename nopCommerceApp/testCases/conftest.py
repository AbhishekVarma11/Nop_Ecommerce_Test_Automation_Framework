from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=='chorme':
        driver=webdriver.Chrome()
        print('launching chorme browser')
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print('launching firefox browser')
    else:
        driver=webdriver.Edge()   
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')
    
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

def pytest_configure(config):
  metadata = config.pluginmanager.getplugin("metadata")
  if metadata:
      from pytest_metadata.plugin import metadata_key
      config.stash[metadata_key]['Project Name'] = 'nop Commerce demo website'
      config.stash[metadata_key]['Module Name'] = 'Admin'
      config.stash[metadata_key]['Tester'] = 'Abhishek'

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce demo website'
#     config._metadata['Module Name'] = 'Admin'
#     config._metadata['Tester'] = 'Abhishek'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    