from yc_etabs_api.yc_etabs_api import ETABS
import ETP001_main as ETP001
import yc_format as ycf


class AutoTrialSection :
    def __init__(self,
                 excel_filename:str = 'input_excel.xls',
                 ) -> None:
        etabs = ETABS()

        self.log = ''
        
        self.current_check = False
        self.max_trial = 1
        self.sub_trial = ycf.sub_trial

        self.log = ''
        self.output_str = ycf.output_str
        self.logging = ycf.logging
        self.output_log = ycf.output_log

        self.excel_filename = excel_filename

        self.etabs = etabs
        self.input_ = self.read_input_excel()

    def read_input_excel(self) -> dict :
        pass

    def anylzing(self) -> None :
        pass

    def adjust_spec_amplification(static_eq:list[float] = [1, 1]) -> float :
        pass

    def designing(self) -> None :
        pass

    def get_design_result(self) -> list :
        pass

    def check_criteria(self) -> bool :
        pass

    def auto_change_sect(self) :
        pass

    def doing (self) :
        priority = 2

        self.log += self.logging('Analyzing... ', priority)
        self.anylzing()

        self.log += self.logging('Adjusting Spectral Amplification... ', priority)
        self.adjust_spec_amplification()


        self.designing()

        self.current_check = self.check_criteria()

    def trying(self) :
        priority = 1

        for trial in range(self.max_trial) :
            real_trial = trial + 1
            
            self.log += self.logging(f'{real_trial}{self.sub_trial(real_trial)}...', priority)
            self.doing

            if self.current_check :
                self.log += self.logging(f'{real_trial}{self.sub_trial(real_trial)} trial is OK!!', priority+1)
                break
            else :
                self.log += self.logging(f'{real_trial}{self.sub_trial(real_trial)} trial is NGGGGGGG!!', priority+1)

                if real_trial == self.max_trial :
                    self.log += self.logging('Trial is MAX trial! Please adjust parameters before do it again!!', priority+2)
                else :
                    self.log += self.logging('CHANGING sections', priority+2)
                    self.auto_change_sect()


if __name__ == '__main__' : 
    AutoTrialSection().doing