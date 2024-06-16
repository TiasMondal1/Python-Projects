from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Boddo chupchap, ki byapar?'
    elif 'hello' in lowered:
        return 'Hello there! Bhalo toh shob?'
    elif 'how are you' in lowered:
        return 'Cholche, tumi bolo'
    elif 'bye' in lowered:
        return 'Thik ache pore kotha hobe abar'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice(['I dont understand','Ki bolchen ta ki?','Onno bhabe bolun']) 