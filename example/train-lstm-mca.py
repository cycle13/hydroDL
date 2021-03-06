from hydroDL import pathSMAP, master
import os

cDir = os.path.dirname(os.path.abspath(__file__))
cDir = r'/home/kxf227/work/GitHUB/pyRnnSMAP/example/'

# define training options
optData = master.updateOpt(
    master.default.optDataCsv,
    path=os.path.join(cDir, 'data'),
    subset='CONUSv4f1',
    tRange=[20150401, 20160401],
)
optModel = master.default.optLstm
optLoss = master.updateOpt(
    master.default.optLoss, name='hydroDL.model.crit.SigmaLoss')
optTrain = master.default.optTrainSMAP
out = os.path.join(cDir, 'output', 'CONUSv4f1_sigma')
masterDict = master.wrapMaster(out, optData, optModel, optLoss, optTrain)

# train
master.train(masterDict, overwrite=True)

# test
pred = master.test(
    out, tRange=[20160401, 20170401], subset='CONUSv4f1', epoch=500)
