import qsharp
import Kitaev
import numpy as np

Check_Message = Kitaev.Import_check.simulate()
print(Check_Message)

if __name__ == '__main__':
    for i in range(5):
        Rz_phi = Kitaev.TestRZ.simulate()
        print(i," TestRZ : ",Rz_phi)
        Rz_phi_bitwise = Kitaev.TestRZ_bitwise.simulate()
        print(i," TestRZ_bitwise : ",Rz_phi_bitwise)

    for i in range(5):
        S_Phi = Kitaev.TestS0.simulate()
        print(i," TestS0 : ",S_Phi)

    for i in range(5):
        S_Phi = Kitaev.TestS1.simulate()
        print(i," TestS1 : ",S_Phi)
        
    for i in range(5):
        H_Phi = Kitaev.TestH.simulate()
        print(i," TestH : ",H_Phi)
