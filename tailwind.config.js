/** @type{import{'tailwind'}.config} */
module.exports = {
    content: [
       'client/templates/client/*.html',
       'core/templates/core/*.html',
       'dashboard/templates/dashbord/*.html',
       'lead/templates/lead/*.html',
       'team/templates/team/*.html',
       'userprofile/templates/userprofile/*.html'
   
    ] ,
   
   theme :{ 
       extend:{}
    },
   Plugin:[]
   
   }