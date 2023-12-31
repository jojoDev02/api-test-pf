from functools import wraps
from flask import Blueprint, jsonify, request
from repositories.user_repository import UserRepository
from auth.auth import AuthManager

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    senha = request.json.get('senha')

    auth_result = AuthManager.authenticate(email, senha)

    if auth_result:
        return jsonify(auth_result), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({'error': 'Authentication token not provided'}), 401

    result = AuthManager.logout(token)
    return jsonify(result)

#verificar fluxo 
@auth_bp.route('/reset-senha', methods=['PUT'])
def update_password():
    dados= request.get_json()
    nova_senha = dados['nova_senha']
    email = dados['email']

    user = UserRepository.update_password(email,nova_senha)
    if user:
        return jsonify({'message':'senha atualizada com sucesso.',
                        'user': user.email,
                         'senha': user.senha })