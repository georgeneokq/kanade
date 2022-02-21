from flask import Flask, request
from os import path
from backend.features.convert import convert_audio

def declare_api_routes(app: Flask):
    @app.route('/api/convert/audio', methods=['POST'])
    def route_convert_audio():
        link = request.json.get('link')
        start_timestamp = request.json.get('start_timestamp')
        end_timestamp = request.json.get('end_timestamp')
        destination = path.join(app.root_path, '..', 'storage', 'audio')
        try:
            info = convert_audio(link, start_timestamp, end_timestamp, destination)
        except Exception as e:
            return {'error': str(e)}, 422  # Unprocessible entity

        return {
            **info,
            'link': f"/download/audio/{info.get('filename')}"
        }