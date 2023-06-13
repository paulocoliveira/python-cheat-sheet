*** Settings ***
Library  SeleniumLibrary
 
*** Variables ***
  
&{options}          browserName=Chrome     platform=Windows 11       version=latest      name=your test name    buildName=your build name        projectName=your project name
&{CAPABILITIES}     LT:Options=&{options}
${REMOTE_URL}       http://%{LT_USERNAME}:%{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub
 
 
*** Keywords ***
 
Open test browser
    Open browser  https://lambdatest.github.io/sample-todo-app/
    ...  remote_url=${REMOTE_URL}
    ...  desired_capabilities=${CAPABILITIES}
 
Close test browser
    Close all browsers