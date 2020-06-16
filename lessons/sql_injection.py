""""
SQL Injection Example
This function is the only one you are permitted
to modify for the lab assignment.

Note: if you aren't familiar with str.format, here
is a link to the docs:
https://docs.python.org/3/library/stdtypes.html#str.format
"""


def create_search_query(account_id: int, search_term: str) -> str:
    """
    Creation of SQL query that has injection vulnerability.
    You should be able to
        1) explain why this is vulnerable,
        2) demonstrate how to exploit this vulnerability, and
        3) modify this code to prevent SQL injection attack
    :param account_id: int
    :param search_term: str
    :return: str (the query)
    """
    # Never do this in the real world...

    #Function Explanation
    #Main purpose is to replace SQL injection pattern string(including specific chracter) to invalid string
     
    #black list  for  SQL Injiection
    sql_injection_format = [ '\'' , '\"' , '-', '=' , '&' , '|' , '%' , ',' , '{', '}', '(' , ')', '$' , '@', '#',
                             'SELECT', 'DELETE', 'DROP', 'UNION', 'GROUP BY', 'IF', 'COLUMN', 'END', 'EXEC', 'DATABASE', 'CONCAT', 'COUNT']

    #Convert the str search_term  into Upper Case
    secure_term = search_term.upper()

    #Replace  the black list patterns  in  secure_term to invaild string
    for format in sql_injection_format:
        secure_term = secure_term.replace(format, "++~~**SqlInjection++~~**")
     
    print(secure_term)
    
    q = 'SELECT * FROM trnsaction ' \
        'WHERE trnsaction.account_id = {} ' \
        'AND ' \
        'trnsaction.memo LIKE "%{}%"'.format(account_id, secure_term)
    return q
