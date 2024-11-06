import pandas as pd

from sasviya.core import Action, Datalib, Table

def test():
    return print("test")

def woe_binning(input_data: pd.DataFrame, nominal_inputs: list[str], cont_inputs: list[str], target: str):
    act_transform = Action("dataPreprocess", "transform")
    # try: d
    # except NameError: d = Datalib().add("/workspaces/myfolder/data/")
    t = Table("credit_data").view(input_data)
    req_pack1 = dict(name='req_intervals',
                inputs=cont_inputs,
                targets=target,
                events='1',
                discretize=dict(method='woe',
                                args = dict(minNBins=3, maxNBins=7)),
                output=dict(scoreWOE=True))
    req_pack2 = dict(name='req_nominals',
                    inputs=nominal_inputs,
                    targets=target,
                    events='1',
                    cattrans=dict(method='woe',
                                args=dict(minNBins=3, maxNBins=7)),
                    output=dict(scoreWOE=True))
    req_packs = []
    req_packs.append(req_pack1)
    req_packs.append(req_pack2)
    woe_transform = act_transform.run(
        table={"name": t.name},
        requestPackages=req_packs,
        casOut=dict(name='woe_transform', replace=True),
        code=dict(casout=dict(name='woe_code', replace=True)),
        copyVars = [target],
        outvarsNameGlobalPrefix='woe'
    )
    return woe_transform

def fetch(table_name, maxrows_n, to_n):
    act_table = Action("table", "fetch")
    return act_table.run(table=table_name, maxrows=maxrows_n, to=to_n)