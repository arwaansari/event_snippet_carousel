from odoo import http
from odoo.http import request


class Events(http.Controller):
    @http.route(['/events'], type="json", auth="public")
    def events(self):
        events = request.env['event.booking'].sudo().\
            search([], order='create_date desc')
        values = [[
                events.name, events.id
            ] for events in events]
        new_list = [values[i:i + 4] for i in range(0, len(values), 4)]
        print('new', new_list)
        return new_list

    @http.route(["/events/event_details"], type="http", auth="public",
                website=True, csrf=False)
    def event_details(self, **kwargs):
        event_id = int(kwargs.get('event_id'))
        event = request.env['event.booking'].search([('id', '=', event_id)])
        values = {}
        values.update({
            'event_id': event
        })
        print(event.booking_date)
        print(values)
        return request.render("event_snippet.event_details1",
                              values)
