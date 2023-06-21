from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask_cors import CORS

import boto3



app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, origins='*') 

@app.route('/run_selenium', methods=['GET'])
def run_selenium():
    def apply_custom_styles():
        driver.execute_script(
            """
        var style = document.createElement('style');
        style.innerHTML = 'body { \
            font-size: 24px !important; \
        } \
        a { \
            text-decoration: underline !important; \
        } \
        input[type="submit"], input[type="button"], button { \
            font-size: inherit; \
            padding: 15px 30px; \
            background-color: orange !important; \
            color: black; \
            border: 2px solid black; \
            border-radius: 5px; \
        }';
        document.head.appendChild(style);
        """
        )

    options = Options()
    options.add_argument("--disable-web-security")
    # Run Chrome in headless mode

    # Configure the ChromeDriver path using ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get("https://www.google.com")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

    apply_custom_styles()

    current_url = ""
    new_url = driver.current_url

    while True:
        if new_url == current_url:
            current_url = new_url
            new_url = driver.current_url
            
        else:
            current_url = new_url
            if current_url == "https://www.google.com/":
                driver.execute_script(
                    """
                    var script = document.createElement('script');
                    script.setAttribute('src', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/js/shepherd.min.js');
                    script.setAttribute('type', 'module');
                    document.body.appendChild(script);
                    script.onload = function() {
                        const tour = new Shepherd.Tour({
                            useModalOverlay: true,
                            defaultStepOptions: {
                                classes: 'shadow-md bg-purple-dark',
                                scrollTo: true,
                                modal: {
                                    styles: {
                                        backgroundColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                },
                                popperOptions: {
                                    modifiers: [
                                        {
                                            name: 'offset',
                                            options: {
                                                offset: [0, 20]
                                            }
                                        },
                                        {
                                            name: 'arrow',
                                            options: {
                                                element: '.shepherd-arrow',
                                                padding: 10
                                            }
                                        }
                                    ],
                                    removeOnDestroy: true
                                },
                                highlightClass: 'shepherd-highlight',
                                classes: 'custom-tooltip-class'
                            }
                        });
                        function speakTooltipText(text) {
                            var speechSynthesis = window.speechSynthesis;
                            var speechText = new SpeechSynthesisUtterance(text);
                            speechSynthesis.speak(speechText);
                        }
                        tour.addStep({
                            id: 'step1',
                            text: 'Enter your search term here then press next.',
                            attachTo: {
                                element: '.SDkEP',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                        text: 'Enable voice guide',
                                        action: function() {
                                                speakTooltipText('Press the button above to view the activities that are happening.');
                                            },
                                        classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press this button to search.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step2',
                            text: 'Press this button to search.',
                            attachTo: {
                                element: '.FPdoLc > center > input[type="submit"]:nth-child(1)',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: function() {
                                        speakTooltipText('Enter your search term then press next.');
                                        tour.back();
                                    },
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Done',
                                    action: tour.complete,
                                    classes: 'custom-done-button-class',
                                },
                            ],
                        });
                        tour.start();
                    };
                    var link = document.createElement('link');
                    link.setAttribute('href', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/css/shepherd.css');
                    link.setAttribute('rel', 'stylesheet');
                    document.head.appendChild(link);
                    var style = document.createElement('style');
                    style.innerHTML = '.custom-tooltip-class .shepherd-content { border: 2px solid black; border-radius: 5px;}'
                                    + '.custom-tooltip-class .shepherd-text {font-size:20px}'
                                    + '.custom-tooltip-class .shepherd-arrow { border-color: black; }'
                                    + '.custom-next-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #177E89!important; color: #FFEEDB; }'
                                    + '.custom-back-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #B484A7 !important; color: #FFEEDB }'
                                    + '.custom-done-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color:  #177E89 !important; color: #FFEEDB; }';
                    document.head.appendChild(style);
                    """
                )
            elif current_url is not None and "https://www.google.com/search?q=" in current_url:
                driver.execute_script(
                    """
                    var style = document.createElement('style');
                    style.innerHTML = 'body { \
                        font-size: 24px !important; \
                    } \
                    a { \
                        text-decoration: underline !important; \
                    } \
                    h3 { \
                        border: 2px solid #ccc; \
                    }';
                    document.head.appendChild(style);
                    """
                )


            elif current_url == "https://www.c3a.org.sg/":
                driver.execute_script(
                    """
                    var script = document.createElement('script');
                    script.setAttribute('src', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/js/shepherd.min.js');
                    script.setAttribute('type', 'module');
                    document.body.appendChild(script);
                    script.onload = function() {
                        const tour = new Shepherd.Tour({
                            useModalOverlay: true,
                            defaultStepOptions: {
                                classes: 'shadow-md bg-purple-dark',
                                scrollTo: true,
                                modal: {
                                    styles: {
                                        backgroundColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                },
                                popperOptions: {
                                    modifiers: [
                                        {
                                            name: 'offset',
                                            options: {
                                                offset: [0, 20]
                                            }
                                        },
                                        {
                                            name: 'arrow',
                                            options: {
                                                element: '.shepherd-arrow',
                                                padding: 10
                                            }
                                        }
                                    ],
                                    removeOnDestroy: true
                                },
                                highlightClass: 'shepherd-highlight',
                                classes: 'custom-tooltip-class'
                            }
                        });

                        // Function to speak the tooltip text
                        function speakTooltipText(text) {
                            var speechSynthesis = window.speechSynthesis;
                            var speechText = new SpeechSynthesisUtterance(text);
                            speechSynthesis.speak(speechText);
                        }
                        
                        tour.addStep({
                            id: 'step1',
                            text: 'Press the button above to view the activities that are happening.',
                            attachTo: {
                                element: 'a[href*="/activities"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                        text: 'Enable voice guide',
                                        action: function() {
                                                speakTooltipText('Press the button above to view the activities that are happening.');
                                            },
                                        classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button above to view the resources.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        
                        tour.addStep({
                            id: 'step2',
                            text: 'Press the button above to view the resources.',
                            attachTo: {
                                element: 'a[href*="/inspiration"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button above to view the courses.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step3',
                            text: 'Press the button above to view the courses.',
                            attachTo: {
                                element: 'a[href*="/short-courses"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button above to view about volunteering opportunities.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step4',
                            text: 'Press the button above to view about volunteering opportunities.',
                            attachTo: {
                                element: 'a[href*="/volunteerism"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button above to view the frequently asked questions.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step5',
                            text: 'Press the button above to view the frequently asked questions.',
                            attachTo: {
                                element: 'a[href*="/faq"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button above to know more information about National Silver Academys.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step6',
                            text: 'Press the button above to know more information about National Silver Academys.',
                            attachTo: {
                                element: 'a[href*="/about-us"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button above to login to your account.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step7',
                            text: 'Press the button above to login to your account.',
                            attachTo: {
                                element: 'a[href*="/user/login?current=/node"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Done',
                                    action: tour.complete,
                                    classes: 'custom-done-button-class',
                                },
                            ],
                        });
                        tour.start();
                    };
                    var link = document.createElement('link');
                    link.setAttribute('href', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/css/shepherd.css');
                    link.setAttribute('rel', 'stylesheet');
                    document.head.appendChild(link);
                    var style = document.createElement('style');
                    style.innerHTML = '.custom-tooltip-class .shepherd-content { border: 2px solid black; border-radius: 5px;}'
                                    + '.custom-tooltip-class .shepherd-text {font-size:20px}'
                                    + '.custom-tooltip-class .shepherd-arrow { border-color: black; }'
                                    + '.custom-next-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #177E89!important; color: #FFEEDB; }'
                                    + '.custom-back-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #B484A7 !important; color: #FFEEDB }'
                                    + '.custom-done-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color:  #177E89 !important; color: #FFEEDB; }';
                    document.head.appendChild(style);
                    """
                )
            elif current_url == 'https://www.c3a.org.sg/activities':
                driver.execute_script(
                    """
                    var script = document.createElement('script');
                    script.setAttribute('src', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/js/shepherd.min.js');
                    script.setAttribute('type', 'module');
                    document.body.appendChild(script);
                    script.onload = function() {
                        const tour = new Shepherd.Tour({
                            useModalOverlay: true,
                            defaultStepOptions: {
                                classes: 'shadow-md bg-purple-dark',
                                scrollTo: true,
                                modal: {
                                    styles: {
                                        backgroundColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                },
                                popperOptions: {
                                    modifiers: [
                                        {
                                            name: 'offset',
                                            options: {
                                                offset: [0, 20]
                                            }
                                        },
                                        {
                                            name: 'arrow',
                                            options: {
                                                element: '.shepherd-arrow',
                                                padding: 10
                                            }
                                        }
                                    ],
                                    removeOnDestroy: true
                                },
                                highlightClass: 'shepherd-highlight',
                                classes: 'custom-tooltip-class'
                            }
                        });
                        // Function to speak the tooltip text
                        function speakTooltipText(text) {
                            var speechSynthesis = window.speechSynthesis;
                            var speechText = new SpeechSynthesisUtterance(text);

                            speechSynthesis.speak(speechText);
                        }
                        
                        tour.addStep({
                            id: 'step1',
                            text: 'Press the button above to view the activities that are happening.',
                            attachTo: {
                                element: 'input#search-bar',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Next',
                                    action: tour.next,
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step2',
                            text: 'Press the button above to view the hotline number.',
                            attachTo: {
                                element: 'a[href*="/inspiration"]',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: tour.next,
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.start();
                    };
                    var link = document.createElement('link');
                    link.setAttribute('href', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/css/shepherd.css');
                    link.setAttribute('rel', 'stylesheet');
                    document.head.appendChild(link);
                    var style = document.createElement('style');
                    style.innerHTML = '.custom-tooltip-class .shepherd-content { border: 2px solid black; border-radius: 5px;}'
                                    + '.custom-tooltip-class .shepherd-text {font-size:20px}'
                                    + '.custom-tooltip-class .shepherd-arrow { border-color: black; }'
                                    + '.custom-next-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #177E89!important; color: #FFEEDB; }'
                                    + '.custom-back-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #B484A7 !important; color: #FFEEDB }'
                                    + '.custom-done-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color:  #177E89 !important; color: #FFEEDB; }';
                    document.head.appendChild(style);
                    """
                )
            elif current_url == "https://www.c3a.org.sg/short-courses":
                driver.execute_script(
                    """
                    var script = document.createElement('script');
                    script.setAttribute('src', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/js/shepherd.min.js');
                    script.setAttribute('type', 'module');
                    document.body.appendChild(script);
                    script.onload = function() {
                        const tour = new Shepherd.Tour({
                            useModalOverlay: true,
                            defaultStepOptions: {
                                classes: 'shadow-md bg-purple-dark',
                                scrollTo: true,
                                modal: {
                                    styles: {
                                        backgroundColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                },
                                popperOptions: {
                                    modifiers: [
                                        {
                                            name: 'offset',
                                            options: {
                                                offset: [0, 20]
                                            }
                                        },
                                        {
                                            name: 'arrow',
                                            options: {
                                                element: '.shepherd-arrow',
                                                padding: 10
                                            }
                                        }
                                    ],
                                    removeOnDestroy: true
                                },
                                highlightClass: 'shepherd-highlight',
                                classes: 'custom-tooltip-class'
                            }
                        });
                        // Function to speak the tooltip text
                        function speakTooltipText(text) {
                            var speechSynthesis = window.speechSynthesis;
                            var speechText = new SpeechSynthesisUtterance(text);

                            speechSynthesis.speak(speechText);
                        }
                        
                        tour.addStep({
                            id: 'step1',
                            text: 'Enter your search term to search for courses.',
                            attachTo: {
                                element: '.filter-course-title',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                        text: 'Enable voice guide',
                                        action: function() {
                                                speakTooltipText('Press the button above to view the activities that are happening.');
                                            },
                                        classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button on the left to choose the price range you prefer.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step2',
                            text: 'Press the button on the left to choose the price range you prefer. Click on the small boxes on the left to select.',
                            attachTo: {
                                element: '.filter-panel.filter-price-range',
                                on: 'right',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button on the left to choose the location you prefer.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step3',
                            text: 'Press the button on the left to choose the location you prefer. Click on the small boxes on the left to select.',
                            attachTo: {
                                element: '.filter-panel.filter-location',
                                on: 'right',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press the button above to apply the filter.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step4',
                            text: 'Press the button above to apply the filter.',
                            attachTo: {
                                element: '.btn.btn-red.mx-auto.btn-cs',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: function() {
                                    speakTooltipText('Press on the courses that you are interested in.');
                                    tour.next();
                                },
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.addStep({
                            id: 'step5',
                            text: 'Press on the courses that you are interested in.',
                            attachTo: {
                                element: '.view-content',
                                on: 'bottom',
                            },
                            classes: 'example-step-extra-class',
                            buttons: [
                                {
                                    text: 'Back',
                                    action: tour.back,
                                    classes: 'custom-back-button-class',
                                },
                                {
                                    text: 'Next',
                                    action: tour.next,
                                    classes: 'custom-next-button-class',
                                },
                            ],
                        });
                        tour.start();
                    };
                    var link = document.createElement('link');
                    link.setAttribute('href', 'https://cdn.jsdelivr.net/npm/shepherd.js@10.0.1/dist/css/shepherd.css');
                    link.setAttribute('rel', 'stylesheet');
                    document.head.appendChild(link);
                    var style = document.createElement('style');
                    style.innerHTML = '.custom-tooltip-class .shepherd-content { border: 2px solid black; border-radius: 5px;}'
                                    + '.custom-tooltip-class .shepherd-text {font-size:20px}'
                                    + '.custom-tooltip-class .shepherd-arrow { border-color: black; }'
                                    + '.custom-next-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #177E89!important; color: #FFEEDB; }'
                                    + '.custom-back-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color: #B484A7 !important; color: #FFEEDB }'
                                    + '.custom-done-button-class { border: 1px solid black; font-size: 16px; padding: 10px 20px; background-color:  #177E89 !important; color: #FFEEDB; }';
                    document.head.appendChild(style);
                    """
                )


    # Close the browser and quit Selenium
    driver.quit()

    # Return a response indicating successful execution
    return jsonify({'message': 'Selenium code executed successfully'})



@app.route('/api/submitForm', methods=['POST'])
def submit_form():
    form_data = request.get_json()
    # Perform any necessary database operations or other actions with the form data
    usernamee = form_data.get('name')
    pw1 = form_data.get('pw')
    pw2 = form_data.get('pw2')

    if not usernamee or not pw1 or not pw2 or pw1!=pw2:
        # Return a failure response if the required fields are missing
        response = {
            'message': 'Form submission failed. Please provide name and email.'
        }
        return jsonify(response), 400
    
    db = boto3.client('dynamodb')
    table_name = 'accounts'
    item = {
        'usernamee': {'S': usernamee},
        'pw': {'S': pw1}
    }
    try:
        # Put the item into the table
        response = db.put_item(TableName=table_name, Item=item)
        print('Data added successfully to DynamoDB table:', table_name)
        
        # Send a response back to the client
        return jsonify({'message': 'Form submitted successfully!'})

    except Exception as e:
        print('Failed to add data to DynamoDB table:', table_name)
        print('Error:', e)
        return jsonify({'message':'Failed to add data to DynamoDB table, error: ' + e})


    

if __name__ == '__main__':
    app.run(debug=True)