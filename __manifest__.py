{
    'name': '4 Events',
    'version': '16.0.1.0.0',
    'sequence': '-1',

    'depends': ['base', 'sale', 'website', 'event_management'],
    'data': [
        'views/snippet_event.xml',
        'views/event.xml',
        'views/event_details_template.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'event_snippet/static/src/js/event_snippet.js',
            'event_snippet/static/src/xml/event_snippet_template.xml',
            'event_snippet/static/src/css/snippet.scss'
        ]
    }
}
