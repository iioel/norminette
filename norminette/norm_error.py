from norminette.colors import red, blue, yellow, pink, grey, green

errors = {
    "SPC_INSTEAD_TAB": "Spaces at beginning of line",
    "TAB_INSTEAD_SPC": "Found tab when expecting space",
    "CONSECUTIVE_SPC": "Two or more consecutives spaces",
    "CONSECUTIVE_WS": "Two or more consecutives white spaces",
    "SPC_BFR_OPERATOR": "missing space before operator",
    "SPC_AFTER_OPERATOR": "missing space after operator",
    "NO_SPC_BFR_OPR": "extra space before operator",
    "NO_SPC_AFR_OPR": "extra space after operator",
    "SPC_AFTER_PAR": "Missing space after parenthesis (brace/bracket)",
    "SPC_BFR_PAR": "Missing space before parenthesis (brace/bracket)",
    "NO_SPC_AFR_PAR": "Extra space after parenthesis (brace/bracket)",
    "NO_SPC_BFR_PAR": "Extra space before parenthesis (brace/bracket)",
    "SPC_AFTER_POINTER": "space after pointer",
    "SPC_LINE_START": "Unexpected space/tab at line start",
    "SPC_BFR_POINTER": "bad spacing before pointer",
    "SPACE_BEFORE_FUNC": "space before function name",
    "TOO_MANY_TABS_FUNC": "extra tabs before function name",
    "TOO_MANY_TABS_TD": "extra tabs before typedef name",
    "MISSING_TAB_FUNC": "missing tab before function name",
    "MISSING_TAB_VAR": "missing tab before variable name",
    "MISSING_TAB_TYPDEF": "Missing tab before typedef name",
    "TOO_MANY_TAB_VAR": "extra tab before variable name",
    "LINE_TOO_LONG": "line too long",
    "EXP_PARENTHESIS": "Expected parenthesis",
    "MISSING_IDENTIFIER": "missing type qualifier or identifier in function arguments",
    "FORBIDDEN_CHAR_NAME": "user defined identifiers should contain only lowercase characters, \
digits or '_'",
    "TOO_FEW_TAB": "Missing tabs for indent level",
    "TOO_MANY_TAB": "Extra tabs for indent level",
    "TOO_MANY_WS": "Extra whitespaces for indent level",
    "SPACE_REPLACE_TAB": "Found space when expecting tab",
    "TAB_REPLACE_SPACE": "Found tab when expecting space",
    "TOO_MANY_LINES": "Function has more than 25 lines",
    "SPACE_EMPTY_LINE": "Space on empty line",
    "SPC_BEFORE_NL": "Space before newline",
    "TOO_MANY_INSTR": "Too many instructions on a single line",
    "PREPROC_NO_SPACE": "Missing space after preprocessor directive",
    "PREPROC_UKN_STATEMENT": "Unrecognized preprocessor statement",
    "PREPROC_START_LINE": "Preprocessor statement not at the beginning of the line",
    "PREPROC_CONSTANT": "Preprocessor statement must only contain constant defines",
    "PREPROC_EXPECTED_EOL": "Expected EOL after preprocessor statement",
    "PREPROC_BAD_IF": "If preprocessor statement without endif",
    "PREPROC_BAD_ELIF": "Elif preprocessor statement without if or elif",
    "PREPROC_BAD_IFDEF": "Ifdef preprocessor statement without endif",
    "PREPROC_BAD_IFNDEF": "Ifndef preprocessor statement without endif",
    "PREPROC_BAD_ELSE": "Else preprocessor statement without if or elif",
    "PREPROC_BAD_ENDIF": "Endif preprocessor statement without if, elif or else",
    "PREPROC_BAD_INDENT": "Bad preprocessor indentation",
    "PREPROC_MULTLINE": "Multiline preprocessor statement is forbidden",
    "PREPOC_ONLY_GLOBAL": "Preprocessor statements are only allowed in the global scope",
    "USER_DEFINED_TYPEDEF": "User defined typedef must start with t_",
    "STRUCT_TYPE_NAMING": "Structure name must start with s_",
    "ENUM_TYPE_NAMING": "Enum name must start with e_",
    "UNION_TYPE_NAMING": "Union name must start with u_",
    "GLOBAL_VAR_NAMING": "Global variable must start with g_",
    "NO_TAB_BF_TYPEDEF": "Missing whitespace before typedef name",
    "GLOBAL_VAR_DETECTED": "Global variable present in file. Make sure it is a reasonable choice.",
    "EOL_OPERATOR": "Logic operator at the end of line",
    "EMPTY_LINE_FUNCTION": "Empty line in function",
    "EMPTY_LINE_FILE_START": "Empty line at start of file",
    "EMPTY_LINE_FUNCTION": "Empty line in function",
    "EMPTY_LINE_EOF": "Empty line at end of file",
    "WRONG_SCOPE_VAR": "Variable declared in incorrect scope",
    "IMPLICIT_VAR_TYPE": "Missing type in variable declaration",
    "VAR_DECL_START_FUNC": "Variable declaration not at start of function",
    "TOO_MANY_VARS_FUNC": "Too many variables declarations in a function",
    "TOO_MANY_FUNCS": "Too many functions in file",
    "BRACE_SHOULD_EOL": "Expected newline after brace",
    "CONSECUTIVE_NEWLINES": "Consecutive newlines",
    "NEWLINE_PRECEDES_FUNC": "Functions must be separated by a newline",
    "NL_AFTER_VAR_DECL": "Variable declarations must be followed by a newline",
    "NL_AFTER_PREPROC": "Preprocessor statement must be followed by a newline",
    "MULT_ASSIGN_LINE": "Multiple assignations on a single line",
    "MULT_DECL_LINE": "Multiple declarations on a single line",
    "DECL_ASSIGN_LINE": "Declaration and assignation on a single line",
    "FORBIDDEN_CS": "Forbidden control structure",
    "SPACE_AFTER_KW": "Missing space after keyword",
    "RETURN_PARENTHESIS": "Return value must be in parenthesis",
    "EXP_SEMI_COLON": "Expected semicolon",
    "EXP_TAB": "Expected tab",
    "NO_ARGS_VOID": "Empty function argument requires void",
    "MISALIGNED_VAR_DECL": "Misaligned variable declaration",
    "MISALIGNED_FUNC_DECL": "Misaligned function declaration",
    "WRONG_SCOPE_COMMENT": "Comment is invalid in this scope",
    "MACRO_NAME_CAPITAL": "Macro name must be capitalized",
    "MACRO_FUNC_FORBIDDEN": "Macro functions are forbidden",
    "ASSIGN_IN_CONTROL": "Assignment in control structure",
    "VLA_FORBIDDEN": "Variable length array forbidden",
    "TOO_MANY_ARGS": "Function has more than 4 arguments",
    "INCLUDE_HEADER_ONLY": ".c file includes are forbidden",
    "INCLUDE_START_FILE": "Include must be at the start of file",
    "HEADER_PROT_ALL": "Header protection must include all the instructions",
    "HEADER_PROT_ALL_AF": "Instructions after header protection are forbidden",
    "HEADER_PROT_NAME": "Wrong header protection name",
    "HEADER_PROT_UPPER": "Header protection must be in uppercase",
    "HEADER_PROT_MULT": "Multiple header protections, only one is allowed",
    "HEADER_PROT_NODEF": "Header protection not containing #define",
    "TERNARY_FBIDDEN": "Ternaries are forbidden",
    "TOO_MANY_VALS": "Too many values on define",
    "NEWLINE_IN_DECL": "Newline in declaration",
    "MULT_IN_SINGLE_INSTR": "Multiple instructions in single line control structure",
    "NEWLINE_DEFINE": "Newline in define",
    "MISSING_TYPEDEF_ID": "Missing identifier in typedef declaration",
    "LABEL_FBIDDEN": "Label statements are forbidden",
    "GOTO_FBIDDEN": "Goto statements are forbidden",
    "PREPROC_GLOBAL": "Preprocessors can only be used in the global scope",
    "WRONG_SCOPE_FCT": "Function prototype in incorrect scope",
    "WRONG_SCOPE": "Statement is in incorrect scope",
    "INCORRECT_DEFINE": "Incorrect values in define",
    "BRACE_NEWLINE": "Expected newline before brace",
    "EXP_NEWLINE": "Expected newline after control structure",
    "ARG_TYPE_UKN": "Unrecognized variable type",
    "COMMENT_ON_INSTR": "Comment must be on its own line or at end of a line",
    "COMMA_START_LINE": "Comma at line start",
    "MIXED_SPACE_TAB": "Mixed spaces and tabs",
    "ATTR_EOL": "Function attribute must be at the end of line",
    "INVALID_HEADER": "Missing or invalid 42 header",
    "INCLUDE_MISSING_SP": "Missing space between include and filename",
    "TYPE_NOT_GLOBAL": "Enums, structs and unions need to be defined only in global scope",
    "FORBIDDEN_TYPEDEF": "Typedef declaration are not allowed in .c files",
    "FORBIDDEN_STRUCT": "Struct declaration are not allowed in .c files",
    "FORBIDDEN_UNION": "Union declaration are not allowed in .c files",
    "FORBIDDEN_ENUM": "Enum declaration are not allowed in .c files",
    "UNEXPECTED_EOF_CHR": "Unexpected end of file (EOF) while parsing a char",
    "UNEXPECTED_EOL_CHR": "Unexpected end of line (EOL) while parsing a char",
    "UNEXPECTED_EOF_MC": "Unexpected end of file (EOF) while parsing a multiline comment",
    "UNEXPECTED_EOF_STR": "Unexpected end of file (EOF) while parsing a string",
    "EMPTY_CHAR": "Empty character constant",
    "CHAR_AS_STRING": "Character constants can have only one character",
    "INVALID_SUFFIX": "This suffix is invalid",
    "BAD_FLOAT_SUFFIX": "Invalid suffix for float/double literal constant",
    "INVALID_BIN_INT": "Invalid binary integer literal",
    "INVALID_OCT_INT": "Invalid octal integer literal",
    "INVALID_HEX_INT": "Invalid hexadecimal integer literal",
    "MAXIMAL_MUNCH": "Potential maximal munch detected",
    "NO_HEX_DIGITS": "No hexadecimal digits followed by the \\x",
    "UNKNOWN_ESCAPE": "Unknown escape sequence",
    "BAD_EXPONENT": "Exponent has no digits",
    "MULTIPLE_DOTS": "Multiple dots in float constant",
    "MULTIPLE_X": "Multiple 'x' in hexadecimal float constant",
}


class NormError:
    def __init__(self, errno, line, col):
        self.errno = errno
        self.line = line
        self.col = col
        self.error_pos = f"(line: {(str(self.line)).rjust(3)}, col: {(str(self.col)).rjust(3)}):\t"
        self.prefix = f"Error: {self.errno:<20} {self.error_pos:>21}"
        self.error_msg = f"{errors.get(self.errno, 'ERROR NOT FOUND')}"
        self.no_color = "\033[0m"
        self.color = self.no_color
        color = {
                "\033[91m": red,
                "\033[92m": green,
                "\033[93m": yellow,
                "\033[94m": blue,
                "\033[95m": pink,
                "\033[97m": grey,
        }
        for key, value in color.items():
            if errno in value:
                self.color = key
                break
        self.prefix = self.prefix
        self.error_msg = self.color + self.error_msg + self.no_color

    def __str__(self):
        return self.prefix + self.error_msg


class NormWarning:
    def __init__(self, errno, line, col):
        self.errno = errno
        self.line = line
        self.col = col
        self.error_pos = f"(line: {(str(self.line)).rjust(3)}, col: {(str(self.col)).rjust(3)}):\t"
        self.prefix = f"Notice: {self.errno:<20} {self.error_pos:>21}"
        self.error_msg = f"{errors.get(self.errno, 'WARNING NOT FOUND')}"

    def __str__(self):
        return self.prefix + self.error_msg
