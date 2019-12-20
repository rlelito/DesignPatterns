from subject import Subject
from real_subject import RealSubject


class Proxy(Subject):
    _log = {'a': None, 'b': None, 'c': None, 'result': ()}

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject: RealSubject = real_subject

    def request(self) -> str:
        if not (self._real_subject.a, self._real_subject.b, self._real_subject.c) == (
                self._log['a'], self._log['b'], self._log['c']):
            result_qe = self._real_subject.request()
            self.log_access(result_qe)
            return f"RealSubject({self._real_subject.a}, {self._real_subject.b}, {self._real_subject.c})" \
                   f" > Executing code.\n\t{result_qe}"
        else:
            return f"RealSubject({self._real_subject.a}, {self._real_subject.b}, {self._real_subject.c})" \
                   f" > Executing same code.\n\t{self._log['result']}"

    def log_access(self, result) -> None:
        print("Proxy: Logging request.")
        self._log = {'a': self._real_subject.a,
                     'b': self._real_subject.b,
                     'c': self._real_subject.c,
                     'result': result}

    @property
    def real_subject(self) -> RealSubject:
        return self._real_subject
