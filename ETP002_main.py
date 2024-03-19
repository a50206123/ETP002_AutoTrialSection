from yc_etabs_api.yc_etabs_api import ETABS
import ETP001_main as ETP001

class AutoTrialSection :
    def __init__(self,
                 excel_filename:str = 'input_excel.xls',
                 ) -> None:
        etabs = ETABS()

        self.log = ''
        
        self.current_check = False
        self.max_trial = 1

        self.excel_filename = excel_filename

        self.etabs = etabs
        self.input_ = self.read_input_excel()

    def read_input_excel(self) -> dict :
        pass

    def anylzing(self) -> None :
        pass

    def adjust_spec_amplication(static_eq:list[float] = [1, 1]) -> float :
        pass

    def designing(self) -> None :
        pass

    def get_design_result(self) -> list :
        pass

    def check_criteria(self) -> bool :
        pass

    def logging(self, log:str) -> None :
        self.log += log + '\n'
        print(log)

    def output_log(self) -> None :
        pass

    def auto_change_sect(self) :
        pass

    def doing (self) :
        self.anylzing()
        self.adjust_spec_amplication()
        self.designing()

        self.current_check = self.check_criteria()

    def sub_trial(trial) :
        sub_trial = 'th'

        if trial in [11, 12] :
            pass
        elif trial % 10 == 1 :
            sub_trial = 'st'
        elif trial % 10 == 2 :
            sub_trial = 'nd'
        elif trial % 10 == 3 :
            sub_trial == 'rd'

        return sub_trial

    def trying(self) :
        for trial in range(self.max_trial) :
            
            print(f'{trial+1}{self.sub_trial(trial+1)}...')

            self.doing

            if self.current_check :
                self.logging(f'{"":-^3s} {trial+1}{self.sub_trial} trial is OK!!')
                break
            else :
                self.logging(f'{"":-^3s} {trial+1}{self.sub_trial} trial is NGGGGGGG!!')

                if trial == self.max_trial-1 :
                    self.logging(f'{"":-^5s} Trial is MAX trial! Please adjust parameters before do it again!!')
                else :
                    self.logging(f'{"":-^5s} CHANGING sections')
                    self.auto_change_sect()


if __name__ == '__main__' : 
    AutoTrialSection().doing