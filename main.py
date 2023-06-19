def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    maleStudents = int(input("How many male students are in the class? "))
    femaleStudents = int(input("How many female students are in the class? "))
    totalStudents = maleStudents + femaleStudents

    m_perc = maleStudents * 100/totalStudents
    f_perc = femaleStudents * 100/totalStudents

    print("The total number of students: " + str(totalStudents))
    print("The number of male and female students: " + str(maleStudents)+ " " + str(femaleStudents))
    print("The percentage of males and females: " + str(m_perc)+ " " + str(f_perc)) 


    return m_perc, f_perc


if __name__ == '__main__':
    main()
