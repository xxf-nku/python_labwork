# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import optparse


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, EOF, SPACE,SUBTRACTION = 'INTEGER', 'PLUS', 'EOF', 'SAPCE', 'SUBTRACTION'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None


    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == ' ':
            token = Token(SPACE, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(SUBTRACTION, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # # we expect the current token to be a single-digit integer
        # left = self.current_token
        # self.eat(INTEGER)
        left = []
        while self.current_token.type == INTEGER or self.current_token.type == SPACE:
            if self.current_token.type == INTEGER:
                left.append(self.current_token)
                self.eat(INTEGER)
            else: self.eat(SPACE)



        # we expect the current token to be a '+' token
        if self.current_token == PLUS:
            op = self.current_token
            self.eat(PLUS)
        else:
            op = self.current_token
            self.eat(SUBTRACTION)



        # # we expect the current token to be a single-digit integer
        # right = self.current_token
        # self.eat(INTEGER)

        right = []
        while self.current_token.type == INTEGER or self.current_token.type == SPACE:
            if self.current_token.type == INTEGER:
                right.append(self.current_token)
                self.eat(INTEGER)
            else:
                self.eat(SPACE)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        left1 = 0
        left_len = len(left)
        for i in range(left_len):
            left1 += left[i].value * (10 ** (left_len-i-1))
        right1 = 0
        right_len = len(right)
        for i in range(right_len):
            right1 += right[i].value * (10 ** (right_len-i-1))
        print(left1, right1)
        if op.value == '+':
           result = left1 + right1
        else: result = left1 - right1
        return result


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
    # 修改代码以允许在输入中使用多位整数，例如“12 + 3”
    # 添加跳过空格字符的方法，以便计算器可以处理带有空格字符（如“ 12 + 3”）的输入
    # 修改代码，而不是“+”处理“-”来计算像“7 - 5”这样的减法