from main import db
from flask import Blueprint, request, jsonify, abort
from models.Moods import Moods
from schemas.MoodSchema import mood_schema
from flask_jwt_extended import jwt_required
from services.auth_decorator import auth_decorator