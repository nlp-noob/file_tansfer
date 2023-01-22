import json

from rich.console import Console
from tqdm import tqdm


user_age_path = ".\\rte_filter_result.json"
input_data_path_list = [
    ".\\age.json",
    ".\\age0001.json",
]

console = Console()

show_context_size = 5


class ResultChecker():
    def __init__(self, input_data_dict, user_age_dict, show_context_size):
        self.input_data_dict = input_data_dict
        self.user_age_dict = user_age_dict
        import pdb;pdb.set_trace()
        self.global_check_step = 0
        self.global_right_cnt = 0
        self.show_context_size = show_context_size
        
    def _display_an_user(self, user_text, dob_info):
        display_list = []
        for order in enumerate(user_text):
            user
            pass
        pass

    def check(self):
        for user_id in self.user_age_dict:
            self.global_check_step += 1
            user_dob_list = user_age_dict[user_id]
            user_text = user_age_dict[user_id]["raw_data"]
            
                
                



def get_age_data():
    df = open(user_age_path, "r")
    user_age_data = json.load(df)
    df.close()
    return user_age_data


def get_merged_input():
    merged_input_dict = {}
    for input_data_path in input_data_path_list:
        df = open(input_data_path, "r")
        data = json.load(df)
        df.close()
        console.print("You are loading the path {}".format(input_data_path), style="green")
        console.print("**"*20, style="yellow")

        for user_id in tqdm(data):
            if user_id not in merged_input_dict:
                merged_input_dict[user_id] = []
            merged_input_dict[user_id].extend(data[user_id]["raw_data"])
    return merged_input_dict

        

def main():
    input_data_dict = get_merged_input()
    user_age_dict = get_age_data()
    resultchecker = ResultChecker(input_data_dict, user_age_dict, show_context_size)
    resultchecker.check()



if __name__ == "__main__":
    main()
    


