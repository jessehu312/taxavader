
from flask import Blueprint, request
from json import load

bp = Blueprint('tax', __name__, url_prefix='/api/tax')

@bp.route('/bracket', methods=['GET'])
def tax_bracket():
    year = request.args.get('year', 2020, type=int)
    bracket = {}
    try:
        with open(f'data/{year}.json') as f:
            bracket = load(f)
    except:
        return 'This year is not available', 404
    return bracket
