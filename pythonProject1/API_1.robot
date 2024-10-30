# Created by aleksey.mitrokhin at 12.07.2024
*** Settings ***
Documentation   Counts attributes
Library   RequestsLibrary
Library   Collections
Library   JSONLibrary
Library   BuiltIn

*** Variables ***
${base_url}   http://10.100.24.147:81/eldoca/app
${Auth_Token}   FycxgaSUgHnBlzMqYn/qsBEm5YBcmX52/eYbm+daUHMkFWLfp7J9PhBERSBxlstBhdbY24o1VoOSR+clASF5CynymWYv5d6NBdLP+TbPT2tw2MaeNw42dWd9B6qwsK5cpdkXnMV1+izcOAAnmvOX8VeVmUlHoj7wKG32BR1x01DghN2lgdPrxRi0iEeiz89q2C1LfJGLqZXemuD71Co54+Bx2ByRaIkxc5RocebzjqI=

*** Test Cases ***
Test GET
    Create Session   my_session   ${base_url}
    &{headers}=   Create Dictionary   Authorization=Bearer${Auth_Token}
    ${response}=   GET On Session   my_session   /documents/1/attributes/count   headers=${headers}
    Log To Console   ${response.status_code}
    Log To Console   ${response.content}