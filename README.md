# Crowdfunding Back End

This is an example back-end for the She Codes Plus course content, to be used by mentors for demonstrating the front-end, or by students to check their deployment/codebase for errors.

This readme doc just contains the bare minimum of information for mentors to be able to hook up a front-end to it. Remember, if you're creating your own readme for the DRF project, you'll need to use the template provided to give a few more details. :) 

### API Spec

| URL                                                   | HTTP Method | Purpose                                                   | Request Body                   | Success Response Code | Authentication/Authorisation |
| ----------------------------------------------------- | ----------- | --------------------------------------------------------- | ------------------------------ | --------------------- | ---------------------------- |
| https://solitary-glitter-2281.fly.dev/api-token-auth/ | POST        | Obtain a JWT to use as authentication at other endpoints. | `{`<br>`"username": ...,`<br>`"password": ...`<br>`}` | 200                   | Supply the correct username/password combo.                             |

