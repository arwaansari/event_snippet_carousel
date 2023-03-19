odoo.define('event_snippet.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
       console.log('ssssss')
           var self = this;
           rpc.query({
               route: '/events',
               params: {},
           }).then(function (result) {
           console.log(result)
            result[0].set_active = true;
            $('.qweb_events').append(Qweb.render('event_snippet.event_template1', {result}));
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});