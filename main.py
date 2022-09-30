from random import randint

'''Αριθμός μητρώου: Π21230'''

'''Μέθοδος για να ανακατέψουμε την λίστα που έχουμε ως όρισμα με πιθανούς συνδυασμούς.
   Προσοχή: Χρησιμοποιούμε μόνο τη βιβλιοθήκη randint για να πάρουμε έναν τυχαίο αριθμό 
   και όχι για μεταθέσεις αριθμών. Εμείς υλοποιήσαμε την δικιά μας συνάρτηση για μετάθεση 
   αριθμών που είναι παρακάτω:'''


def shuffleMyList(lst):
    a = len(lst)

    for i in range(0, a):
        rand = randint(i, a-1)
        lst[i], lst[rand] = lst[rand], lst[i]


def thresh(lst, t):
    output = []
    lastOutput = []
    characters = ''

    for a in lst:
        char = str(a)
        characters += char

    count = 0
    while len(output) != len(lst) * 2:
        count += 1
        l1 = list(characters)

        shuffleMyList(l1)

        result = int(''.join(l1))
        if result not in output:
            output.insert(count, result)

    for element in output:
        if element > t:
            lastOutput.append(element)

    lastOutput.sort()

    '''Αν θέλουμε να κάνουμε print την τελική λίστα χρησιμοποιούμε τη συνάρτηση
    print(lastOutput)'''
    '''Επιστροφή δυνατών αριθμών που φτιάχνουμε με τα ψηφία της λίστας αν τα ενώσουμε. Είναι και σορταρισμένα, 
    όπως ακριβώς φαίνεται και στο παράδειγμα που δόθηκε.'''
    return lastOutput


'''Η λίστα περιέχει ψηφία που δεν επαναλαμβάνονται. Π.χ, η παρακάτω λίστα έχει το 1,2,3.
Για την κλήση της συνάρτησης thresh(lst, t), γράφουμε:'''

'''thresh([1, 2, 3], 200)'''
