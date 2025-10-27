*** Settings ***
Library           ../resources/keywords.py
Variables         ../resources/variables.py

*** Test Cases ***
Ping Network Host
    [Documentation]    Verify that the host is reachable
    ${status}=    Verify Connection    ${HOST}
    Should Be True    ${status}

Measure Latency
    [Documentation]    Measure the latency to host
    ${latency}=    Check Network Latency    ${HOST}
    Should Be True    ${latency} > 0
