from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from QWeb.internal import browser, exceptions
from robot.libraries.BuiltIn import BuiltIn

NAMES = {
    'chrome': 'chrome',
    'ie': 'internet explorer',
    'internet explorer': 'internet explorer',
    'edge': 'MicrosoftEdge',
    'firefox': 'firefox',
    'ff': 'firefox',
    'safari': 'safari'
}


def open_browser(kobiton_browser, kobiton_device, kobiton_os, kobiton_os_version):
    try:
        desired_caps = {
            'sessionName': BuiltIn().get_variable_value('${PROJECTNAME}') or 'Test Automation',
            'sessionDescription': '',
            'deviceOrientation': BuiltIn().get_variable_value('${ORIENTATION}') or 'landscape',
            'captureScreenshots': True,
            'browserName': kobiton_browser,
            'deviceGroup': 'KOBITON',
            'deviceName': kobiton_device,
            'platformVersion': kobiton_os_version,
            'platformName': kobiton_os,
        }
    except KeyError as e:
        raise exceptions.QWebException('Incorrect Kobiton capabilities: "{}"'.format(e))
    try:
        driver = webdriver.Remote(
            command_executor=BuiltIn().get_variable_value('${KOBITONURL}'),
            desired_capabilities=desired_caps)
    except WebDriverException as e:
        raise exceptions.QWebException('Incorrect Kobiton capabilities: "{}"'.format(e))
    browser.cache_browser(driver)
    return driver
