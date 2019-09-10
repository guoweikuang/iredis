def test_zcount(judge_command):
    judge_command(
        "zcount foo -10 0",
        {"command_key_min_max": "zcount", "key": "foo", "min": "-10", "max": "0"},
    )


def test_bzpopmax(judge_command):
    judge_command(
        "bzpopmax set set2 set3 4",
        {"command_keys_timeout": "bzpopmax", "keys": "set set2 set3", "timeout": "4"},
    )
    judge_command(
        "bzpopmin set   4",
        {"command_keys_timeout": "bzpopmin", "keys": "set", "timeout": "4"},
    )


def test_zadd(judge_command):
    judge_command(
        "zadd t 100 qewqr 23 pp 11 oo",
        {
            "command_key_condition_changed_incr_score_members": "zadd",
            "key": "t",
            "score": "11",  # FIXME: only have last one
            "member": "oo",
        },
    )
    judge_command(
        "zadd t incr 100 foo",
        {
            "command_key_condition_changed_incr_score_members": "zadd",
            "key": "t",
            "incr": "incr",
            "score": "100",  # FIXME: only have last one
            "member": "foo",
        },
    )
    judge_command(
        "zadd t NX CH incr 100 foo",
        {
            "command_key_condition_changed_incr_score_members": "zadd",
            "key": "t",
            "condition": "NX",
            "changed": "CH",
            "incr": "incr",
            "score": "100",  # FIXME: only have last one
            "member": "foo",
        },
    )


def test_zincrby(judge_command):
    judge_command(
        "zincrby t 10 foo",
        {
            "command_key_float_member": "zincrby",
            "key": "t",
            "float": "10",
            "member": "foo",
        },
    )
    judge_command(
        "zincrby t 2.3 foo",
        {
            "command_key_float_member": "zincrby",
            "key": "t",
            "float": "2.3",
            "member": "foo",
        },
    )


def test_zlexcount(judge_command):
    judge_command(
        "zlexcount a - +",
        {
            "command_key_lexmin_lexmax": "zlexcount",
            "key": "a",
            "lexmin": "-",
            "lexmax": "+",
        },
    )
    judge_command(
        "zlexcount a (aaaa [z",
        {
            "command_key_lexmin_lexmax": "zlexcount",
            "key": "a",
            "lexmin": "(aaaa",
            "lexmax": "[z",
        },
    )
    judge_command(
        "ZLEXCOUNT myzset - [c",
        {
            "command_key_lexmin_lexmax": "ZLEXCOUNT",
            "key": "myset",
            "lexmin": "-",
            "lexmax": "[c",
        },
    )
    judge_command(
        "ZLEXCOUNT myzset [aaa (g",
        {
            "command_key_lexmin_lexmax": "ZLEXCOUNT",
            "key": "myset",
            "lexmin": "[aaa",
            "lexmax": "(g",
        },
    )
