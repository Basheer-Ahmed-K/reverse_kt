def scope_test():
    def local():
        spam = "I am local scope"

    def non_local():
        nonlocal spam
        spam = "I am non local"

    def do_global():
        global spam
        spam = "I am global"

    spam = "test spam"
    local()
    print("after local:", spam)
    non_local()
    print("after non local:", spam)
    do_global()
    print("after global:", spam)


scope_test()
print("the global", spam)
