import xml.etree.ElementTree as ET

def parse_results(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Assuming there's only one testsuite element under testsuites
    testsuite = root.find('testsuite')
    
    if testsuite is not None:
        total_tests = int(testsuite.attrib['tests'])
        failures = int(testsuite.attrib['failures'])
        errors = int(testsuite.attrib['errors'])
        skipped = int(testsuite.attrib['skipped'])
        passed = total_tests - (failures + errors + skipped)
        pass_percentage = (passed / total_tests) * 100
        return pass_percentage, passed, total_tests
    else:
        raise KeyError("'testsuite' element not found in the XML file")

result_file = 'results.xml'
try:
    pass_percentage, passed, total_tests = parse_results(result_file)
    print(f"Total Tests: {total_tests}")
    print(f"Passed Tests: {passed}")
    print(f"Pass Percentage: {pass_percentage:.2f}%")
except KeyError as e:
    print(f"Error: {e}")
except ET.ParseError as e:
    print(f"XML Parse Error: {e}")
