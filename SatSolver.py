import sys
from copy import deepcopy


class SatSolver:

    def __init__(self, path):
        self.true = set()
        self.false = set()
        cnf = self.input_cnf(path)
        self.print_cnf(cnf, 'Original CNF:=')
        self.solve(cnf)

    def dpll(self, cnf):
        units = []
        true = []
        false = []
        cnf = list(set(cnf))

        for clause in cnf:
            if len(clause) < 3:
                units.append(clause)

        print('\n')
        self.print_cnf(cnf, 'Initial CNF:=')

        if len(units):
            for unit in units:
                if '~' in unit:
                    false.append(unit)
                    self.false.add(unit)
                    i = 0
                    while True:
                        if i < len(cnf):
                            if unit in cnf[i]:
                                cnf.remove(cnf[i])
                                i -= 1
                            elif unit[-1] in cnf[i]:
                                cnf[i] = cnf[i].replace(unit[-1], '').strip()
                                if '  ' in cnf[i]:
                                    cnf[i] = cnf[i].replace('  ', ' ')
                            i += 1
                        else:
                            break
                else:
                    true.append(unit)
                    self.true.add(unit)
                    i = 0
                    while True:
                        if i < len(cnf):
                            if '~' + unit in cnf[i]:
                                cnf[i] = cnf[i].replace('~' + unit, '').strip()
                                if '  ' in cnf[i]:
                                    cnf[i] = cnf[i].replace('  ', ' ')
                            elif unit in cnf[i]:
                                cnf.remove(cnf[i])
                                i -= 1
                            i += 1
                        else:
                            break

        self.print_cnf(cnf, 'Updated CNF:=')
        self.print_cnf(units, 'Unit Clauses:=')

        for clause in cnf:
            if len(clause) == 0:
                print('\t!!!ERROR......ERROR!!!')
                for i in true:
                    self.true.remove(i)
                for i in false:
                    self.false.remove(i)
                return False

        # print('TRUE SET : ', self.true)
        # print('FALSE SET : ', self.false)
        # print('TRUE : ', true)
        # print('FALSE : ', false)

        if not len(cnf):
            return True

        variables_new = [i for i in list(set(''.join(cnf))) if i.isalpha()]

        if self.dpll(deepcopy(cnf) + [variables_new[0]]):
            return True

        elif self.dpll(deepcopy(cnf) + ['~' + variables_new[0]]):
            return True

        else:
            for i in true:
                self.true.remove(i)
            for i in false:
                self.false.remove(i)
            return False

    def solve(self, cnf):

        variables = [i for i in list(set(''.join(cnf))) if i.isalpha()]

        if self.dpll(cnf):
            print('\n')
            print('\t\tResult: SATISFIABLE')
            solution = ''

            for tr in self.true:
                solution += ('('+tr+')')
                # print('\t\t', tr, '= 1')
            for fl in self.false:
                solution += ('('+fl[-1]+ '\u0305'+')')
                # print('\t\t', fl[-1], '= 0')
            print('\t\tSolution:', solution)
            return True
        else:
            print('\n')
            print('\t\tResult: UNSATISFIABLE')
            return False

    def input_cnf(self, path):
        cnf = []
        file = open(str(path), 'r')

        line = file.readline()

        while line:
            cnf.append(str(line).upper().strip())
            line = file.readline()

        file.close()

        return list(set(cnf))

    def print_cnf(self, cnf, message=''):
        k = ''
        for clause in cnf:
            clause = list(clause.replace(' ', ''))
            i = 0
            while True:
                if i < len(clause):
                    if clause[i] == '~':
                        clause = clause[:i] + clause[i + 1:]
                        clause[i] = (str(clause[i]) + '\u0305')
                    i += 1
                else:
                    break
            clause = str(' + '.join(clause))
            k += ('(' + clause + ')').strip()

        if message == '':
            print(str(k))
        else:
            print(str(message), str(k))


ss = SatSolver('input.txt')
