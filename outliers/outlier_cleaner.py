#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    percent = int(round(len(ages)*10/100))
    print "asdfsad",percent
    # list_tup = zip((ages).tolist(),(net_worths).tolist(),((net_worths-predictions)**2).tolist())
    list_tup = sorted(zip((ages).tolist(),(net_worths).tolist(),((net_worths-predictions)**2).tolist()),
                      reverse=True,key=lambda x:x[2])
    print "Sorted", list_tup , len(list_tup)
    print "Scliced",  list_tup[percent:] , len(list_tup[percent:])
    cleaned_data = list_tup[percent:]
    # print "Sorted by error >>>" , sorted(list_tup,reverse=True,key=lambda x:x[2])[0:10]
    # sorted_tup = sorted(list_tup,reverse=True,key=lambda x:x[2])[0:percent]
    # list_indexes = []
    # for i in xrange(len(sorted_tup)):
    #     list_indexes.append(list_tup.index(sorted_tup[i]))
    # print "List indexes >>>>>>>>",list_indexes
    # print "Total Before", len(sorted_tup)
    # for loop in range(1,len(list_indexes) + 1):
    #     print "List indexedasdf",list_indexes[loop - 1]
    #     list_tup.pop((list_indexes[loop - 1]))
    # print "Total After", len(list_tup)
    # cleaned_data = list_tup
    #
    # list_test12 = [1,4,2,3,6]
    # print "Pop Demo", list_test12.pop(0)
    # print "Pop Demo1", list_test12.pop(1),list_test12.pop(2),list_test12.pop(3),list_test12.pop(4)

    return cleaned_data

    # #square difference between actual and prediction
    # errors = (net_worths-predictions)**2
    # #cluster cleaned data
    # cleaned_data = zip(ages,net_worths,errors)
    # #sort clustered data by second item in each tuple
    # cleaned_data = sorted(cleaned_data,key=lambda x:x[2][0], reverse = True)
    # #keep only 90% observations
    # limit = int(len(net_worths)*0.1)
    #
    # return cleaned_data[limit:]

    # import numpy as np
    # from operator import itemgetter
    # cleaned_data = []
    # errors = abs(predictions - net_worths)
    # cleaned_data = zip(predictions, ages, errors)
    # cleaned_data_sorted = sorted(cleaned_data, key = itemgetter(2)) #sort by error.
    # cleaned_data = cleaned_data_sorted[:81]


    ### your code goes here
    import numpy
    # error = predictions - net_worths
    # error_sorted = sorted(error,reverse=1)
    # error_sliced = error_sorted[0:10]

    # test_tup = [i[2] for i in list_tup]
    # print "list", [i[2] for i in list_tup]
    # print "Len len(net_worths)" , len(error_sliced)
    # cleaned_data = list()
    # for y in xrange(len(net_worths)):
    #     error_loop = (predictions[y] - net_worths[y])
    #     for err in xrange(len(error_sliced)):
    #         if ( error_loop <> error_sliced[err]):
    #             tup = ages[y],net_worths[y],error_loop
    #             print "Tuple " , tup
    #             print "error_sliced", error_sliced[err]
    #             tup = []
    #             cleaned_data.append(tup)
    # print "List count >>>" , len(cleaned_data)
    # print "Clean Data?>> ", cleaned_data

    # ages       = numpy.reshape( numpy.array(ages), numpy.array(len(ages), 1))
    # net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    # test = numpy.array([9,1,3,4,8,7,2,6,0,10,4,5])
    # test_sorted = sorted(test,reverse=1)
    # print "Test Soreted >>" ,test_sorted[10:len(test_sorted)]
    # print "Test>>>",test
    # print "Tesat sorted" , test_sorted
    # print "Arg Sort ", numpy.argsort(test)
    # temp = numpy.argpartition(-test, 4)
    # result_args = temp[:4]

    # temp = numpy.partition(-test, 2)
    # result = -temp[2:]
    # print "Result >>" , temp
    # print "Result >>" , result

    # return cleaned_data

