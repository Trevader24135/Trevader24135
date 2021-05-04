#singleinstance force

::%shawzin::
gui, new, -MaximizeBox -MinimizeBox +AlwaysOnTop, Shawzin Songs
gui, show, w100 h200
gui, Add, Button, x0 y0 w100 h25 gShawzinUnravel, Unravel
gui, Add, Button, x0 y25 w100 h25 gShawzinAllStar, All-Star
gui, Add, Button, x0 y50 w100 h25 gShawzinDueloftheFates, Duel of the Fates
gui, Add, Button, x0 y75 w100 h25 gShawzinHesaPirate, He's a Pirate
gui, Add, Button, x0 y100 w100 h25 gShawzinAlone, Alone
gui, Add, Button, x0 y125 w100 h25 gShawzinNyanCat, Nyan Cat (slow)
gui, Add, Button, x0 y150 w100 h25 gShawzinNumb, Numb
gui, Add, Button, x0 y175 w100 h25 gShawzinSoviet, Soviet Anthem
return

ShawzinUnravel() {
clipboard := "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"
}

ShawzinAllStar() {
clipboard := "6EAARAJKAOKATJAdEAiEAnMAtKA2KA7JBAJBFEBKEBTRBYKBdKBiJBnJBsEBxEB2BB7ECbECgRClKCqKCvJC0JC4EC+MDIKDRKDWJDbJDgEDlRDvKD5KD9JEDEENEESJEXBEhEE4BE+EFBEFFEFKEFNEFPEFREFUEFZEFeEFgEFoEFtEFwEFyEF3EF5EF7EF9JGBKGFEGIKGPRGUMGZKGeKGgJGjJGoJGtEG0KG3EG8EHAEHGBHIEHKEHPBHUKHeRHhKHmSHoKHtRHwKH0SH3KH8RIBMIGKILJIQJIVJIYJIaEIfEIuEIyEI3EI6EI8EJBJJSKJUEJZEJeEJhEJjBJoKJ7EKAEKKBKMEKPEKUEKdBKfEKiEKnEKwKK6KLIELOELXBLaELcELhELrBLtELvEL0EL+KMJKMYRMiMMrKMvJM1JM6ENDENSENXJNbENgKNlJNqJN5EOCJOIKOSBOXEOrBOyEO1EO5EO+EPBEPDEPFEPIEPNEPSEPUEPcEPgEPjEPlEPqEPtEPvEPxJP0KP5EP8KQDRQHMQNKQRJQXJQcJQlEQnJQqKQsEQxEQ3EQ7BQ+ERAERFKRLRRPSRVKReERkERmKRxRR2MR8MSAKSDJSFESLESQSSaRSeRSkKSuESzES2BTFETHJTJKTMETPETRETUETWETbBTgKT0ET5EUEBUGEUIEUNEUWBUYEUaEUgEUqKU0KVDEVIEVSBVUEVXEVcEVmBVoEVrEVwEV6KWEKWTRWdMWmKWqJWwJW1EW/EXOEXTJXYEXcKXhJXnJX1EX+JYEKYNBYSRYvKY5JZCEZIKZRMZbKZgJZqEZuBZzBZ4RZ9KaHJaREaWKagMapKauJa4Ea8BbBBbGRbLKbVJbfEbkKbtMb3Kb8JcFEcKBcPBcURcZKciJcsEcxKc7MdEKdJJdSEdXKdnEdsEd2Bd5Ed7EeAEeJBeMEeOEeUEeeKenKe2Ee6EfEBfGEfJEfOEfXBfaEfcEfhEfrKf1KgERgOMgXKgcJghigmhgwEg/EhEJhIEhNKhSJhXEhlRhvKhzKh4JiCEiHEiMMiRKiaKifJikJipEivJi0Ei5Ri+KjCKjHJjMJjREjWEjbBjgKkCRkHRkMKkVJkaJkdKkoRktMkyMk2Kk5Jk8ElAElFBlLJlQElWRlbKlkKlpJlvElzEl4Jl+KmHSmhRmoRmqRmvRm0Rm2Rm5Rm7Rm+RnCRnHRnKRnRRnWRnZRnbRnfRniRnkRnnRnpSnuRnwKn4Rn8MoBKoGKoJJoLJoQJoVEodKogEolEopEouBoxEo0Eo4BpAKpJRpMKpRSpUKpZRpdKphSpkKppRpuMpzKp4Jp9JqCJqFJqHEqMEqaEqfEqkEqnEqpEqvSrCRrHRrMRrPRrRRrWKrqErvEr4Br7Er9EsDEsMBsOEsREsVEsfKsqKs4Es9EtHBtJEtMEtREtbBtdEtgEtkEtuKt4KuHRuRMuaKufJukiuqhuzEvDEvHJvNEvRKvWJvbJvoEvyJv3KwAEwFKwjRwtMw2Kw7JxAixFhxPExeExjJxoExtKxxJx3JyEEyOJyTKycByh"
}

ShawzinDueloftheFates() {
clipboard := "6MAARADMAHKAIJAJMANRAROAVJAXMAbRAeMAiKAjJAkMAoRAsMAvKAwJAxJA8KBAMBDRBKBBQRBXMBdKBgJBkJBxKB0MB3RB+BCFRCLMCSKCVJCYJClJCoKCsMCyBC5SC/RDGMDJKDMJDZJDdKDgMDnBDtRD0MD7KD9JEBMEHRELMEOKEQJERMEVREYMEbKEdJEeMEhRElOEpJErMEvREyME2KE3JE4JFDKFGMFKRFSBFYRFfMFmKFpJFsJF5KF9MGARGHBGNRGUMGbKGeJGhJGvJGyKG1MG8BHDSHJRHPMHTKHWJHkJHnKHrMHxBH4RH+MIFKIIJIMMISRIVMIYKIaJIbMIfRIiOImJIpMItRIxMI0KI2JI3MI7RI+MJCKJDJJEMJIRJMMJPKJQJJSMJVRJZMJdKJeJJfMJjRJnMJqKJrJJtMJxRJ0MJ4KJ5JJ6"
}

ShawzinHesaPirate() {
clipboard := "3CAAKACRAFRAKRAPUARhAThAYhAdkAfUAiUAnRArKAuKAwRAzCA6KA8RA+RBDRBIUBLhBNhBShBXkBZUBbUBgRBlKBnRBqCBzKB2RB4RB9RCChCEkCHkCLkCQkCTkCVkCahCeUChhCjRCmRCtUCvhCyhC3kC7kDARDDRDKhDMUDOUDThDYRDaUDdCDnKDpRDrRDwRD1UD3hD6hD/hEDkEGUEIUENRESKEUKEWREZCEgKEjRElREqREvUExhEzhE4hE9kE/UFCUFHRFLKFORFQCFaKFcRFfRFjRFohFqkFtkFykF2kF5kF7kGAhGFUGHhGKRGMRGTUGWhGYhGdkGikGmRGpRGwhGzUG1UG6RG+MHBRHDRHIUHNhHShHXhHZkHbkHghHjhHqRHsCHukH9kIGRIJEILUIaUIcRIhhIohIykI0kI2kI7kJAhJFkJHUJTUJYUJdUJihJkkJwkJ1kJ6hJ/kKBkKNhKSUKXRKbRKlUKnhKqkKzkK2kK4hK9ULChLGkLLkLQkLVhLekLhkLjkLthLvULyhL3UL7RMAUMKKMMRMORMYUMahMdUMnhMpkMrhMwkM1kM6kM/hNDRNIRNSUNUhNXkNbkNgRNlRNqkNvhNzkN9UN/ROCUOLMOOROQkOehOthOyhO2UO7kO+kPKhPYhPnkPrUPwRP1RP8UP+hQBkQDRQLUQNhQPhQSRQZUQbhQekQgkQlhQqkQvkQxkQ9hRLhRakRfURjRRo"
}

ShawzinAlone() {
clipboard := "3iAAhAESAJMAdJAxiBFEBZEB0EB2BB5BB7ECeMCjSCoMC8JDPiDjED3BEQEESEEVBEXBEaSEyhE8iFGiFLiFQhFVhFXSFciFpMFuMFzMF4SF9MF/EGEBGQiGViGaiGfEGkMGniG4hG9hHChHHEHMMHOiHkiHpiHuhHzhH2SH7iIHMIMMIRMIWSIbMIdEIiBIviI0iI5iI+EJCMJFMJWMJbSJliJvSJ5iJ+SKDEKKMKSEKXBKaEKcBKfEKgiKlSKqJKyMK5JK+ELCJLDELHBLIiLNMLSELZMLhELmBLpELrBLuELwiL1ML6EMBMMIiMNhMRiMShMWiMXhMciMhhMpEMwEM1BM5EM6BM+SM/hNBiNEJNJENQiNYJNdENgJNhENlBNmENrMNwEN4MN/EOEBOIEOJBONEOOBOTMOYSOiiOsSO2iO7yPAhPHEPOSPTEPXSPYEPchPdiPiSPnMP7JQPiQiEQ2ERRERUBRWBRZER8MSASSFMSZJStiTBETVBTtETwETyBT1BT3MUQEUVSUahUfSUhSUkMU4SU6EU9SVBEVGSVJSVLMVfEVkSVphVuSVwiVzMV9EWEhWHiWJEWMMWOiWRiWWBWYhWbSWuhW4iXCiXHiXMhXRhXTSXYiXlMXqMXvMX0SX5MX7EYABYMiYRiYWiYbEYgMYjiY0hY5hY+hZDEZIMZKiZgiZliZqhZvhZySZ3iaDMaIMaNMaSSaXMaZEaeBariawia1ia6Ea/MbBMbSMbXSbhibrSb1ib6Sb/EcGMcOEcTBcWEcYBcbEcdichScmJcuMc1Jc6Ec+Jc/EdDBdEidJMdOEdVMddEdiBdmEdnBdqEdsidxMd2Ed9MeEieJheNieOheSieTheYiedhelEesEexBe1Ee2Be6Se7he9ifAJfFEfMifUJfZEfcJfeEfhBfiEfnMfsEf0Mf7EgABgEEgFBgJEgKBgPMgUSgeigoSgyig3yg8hhDEhKShPEhTShUEhYhhZiheJhjEhrihyJh3Eh7Jh8EiABiBEiGMiLEiSMiaEifBiiEijBinEioiitMiyii6BjBBjGijKBjLijPhjQMjVijahjhEjpEjuBjxEjzBj2Sj4hj6ij9JkBEkJikQJkVEkZJkaEkeBkfEkkMkpEkwMk4Ek9BlBElCBlGElHBlMMlRSlbilkSluilzSl4"
}

ShawzinNyanCat() {
clipboard := "3hAAkACRAERAFEAHMAIKAJEAKEAMKAOMAQMASKATEAUKAVRAWhAXkAYRAZhAaKAbRAcEAdKAeEAfRAghAikAkRAlhAmKAnRAoEApMAqRArMAsKAtEAuKAvMAwEAyKAzRA0hA1KA2RA3KA4EA5KA6EA8KA+hBAkBCRBERBFEBHMBIKBJEBKEBMKBOMBQMBSKBTEBUKBVRBWhBXkBYRBZhBaKBbRBcEBdKBeEBfRBghBikBkRBlhBmKBnRBoEBpMBqRBrMBsKBtEBuKBvMBwEByKBzRB0hB1KB2RB3KB4EB5KB6EB8"
}

ShawzinNumb() {
clipboard := "6KAERAIKAMEAOKAPSAQhAbUAoEAuMAvSAwKBERBIKBMKBORBPhBQUBcRBoCBuJBvRBwKCERCIKCMECOKCPSCQBCUBCYhCbBCgBCkUCoBCsECuMCvSCwMC0MC4MC8MDAKDERDIKDMKDORDPhDQEDUEDYUDcEDgEDkRDoEDsCDuJDvRDwRD0RD4RD8REAKEEREIKEMBEOEEPKEQKEYKEcKEgKEkMEoKEsBEuEEvMEwKE0JE4EE8EFNKFORFPKFQKFUJFYEFcJFkCFtJFuRFvKFwKF0JF4EF8JGEBGOEGPKGQKGYKGcKGgKGkMGoKGsBGuEGvMGwKG0JG4EG8EHNKHORHPKHQKHUJHYEHcJHkJHsCHtJHuRHvKHwJH0EH8JIEKIMBIOEIPKIQKIYKIaKIeKIgKIkKImBIrBItEIuMIvKIwKIyKI2KI4KI8KI+KJIKJMEJNKJORJPSJQSJURJYKJcKJoKJsCJtJJuRJvSJwSJ4RJ8KKAMKIRKMBKOEKPKKQKKYKKaKKeKKgKKkKKmBKrBKtEKuMKvKKwKKyKK2KK4KK8KK+BLNELOKLPSLQSLcSLgRLoBLtELuMLvSLwSL4SL8SMAUMIEMOKMPRMQSMcSMgRMoCMtJMuRMvSMwSM4SM8SNARNIBNNENOKNPSNQSNYSNcBNdENeKNfSNgRNoBNtENuMNvSNwSN4SN8BN9EN+MN/SOAUOIEOOKOPROQSOYSOcEOdKOeROfSOgROoCOtJOuROvSOwSO4SO8CO9JO+RO/SPARPIBPNEPOKPPSPQSPYSPcSPgSPkRPoSPsBPuEPvMPwRP0RP4RP8EQNKQORQPSQQRQURQYRQcKQkKQsCQtJQuRQvMQwKQ0JQ8KREKRMBROERPKRQKRYKRcKRgKRkMRoKRsBRuERvMRwKR0JR4ER8ESNKSORSPKSQKSUJSYEScJSkJSsCStJSuRSvKSwJS0ES8JTEKTMBTOETPKTQKTYKTaKTeKTgKTkKTmBTrBTtETuMTvKTwKTyKT2KT4KT8KT+KUIKUMEUNKUORUPSUQSUURUYKUcKUoKUsCUtJUuRUvSUwSU4RU8KVAMVIRVMBVOEVPKVQKVYKVaKVeKVgKVkKVmBVrBVtEVuMVvKVwKVyKV2KV4KV8KV+KWIKWMEWNKWORWPSWQSWURWYKWcKWkKWoKWsCWtJWuRWvhWwUW2hW8UXIBXNEXOKXPSXQSXcSXgRXoBXtEXuMXvSXwSX4SX8SYAUYIEYOKYPRYQSYcSYgRYoCYtJYuRYvSYwSY4SY8SZARZIBZNEZOKZPSZQSZYSZcBZdEZeKZfSZgRZoBZtEZuMZvSZwSZ4SZ8BZ9EZ+MZ/SaAUaIEaOKaPRaQSaYSacEadKaeRafSagRaoCatJauRavSawSa4Sa8Ca9Ja+Ra/SbARbIBbNEbOMbPSbQBbUEbYMbcEbgSbkhboUbsCbuJbvRbwJb0Rb4Jb8CcAScEUcIBcNEcOKcPhcQEcUKcYEccUcgCckKcoCcsEctKcuRcvhcwEc0Kc4Rc8UdARdEKdISdMBdNEdOMdPSdQBdUEdYMdcEdgSdkhdoUdsCduJdvRdwJd0Rd4Jd8CeAJeEUeISeMCeNKeORePUeQUeUUecUekUeoSesCetKeuRevUewUe0Ue8UfEhfIUfMKfQKfUKfYKfcKfgKfkKfoCfsBftEfuKfvSfwSf8SgARgIBgNEgOMgPSgQSgYSgcSggUgoEguKgvRgwSg8ShARhIChNJhORhPShQShYShcShgRhoBhtEhuKhvShwSh4Sh8Bh9Eh+Kh/SiARiIBiNEiOMiPSiQSiYSicBidEieMifSigUioEiuKivRiwSi4Si8Ei9Ki+Ri/SjARjICjNJjORjPSjQSjYSjcCjdJjeRjfSjgRjoBjtEjuKjvSjwhj7UkIEkOMkPSkQKkkRkoKksKkuRkvhkwUk8RlIClOJlPRlQ"
}

ShawzinSoviet() {
clipboard := "6RAAhAHRAUSAeUAhKAvKA1SA8RBLMBURBZEBnEBuJB1JCDKCKMCQMCeRClSCsUC5hDEiDHRDdkDjiDwhD6iD+UELREShEZUEnSEyUE2KFFKFMSFTRFiMFrRFwEF+EGFhGMUGbSGlRGpRGwhG3iG+kHFkHUiHjhHqUHyhH5iIARIURIahI3UJTSJaRJhSJnUJvKKEKKLSKmRKzMK8RLBELOELVhLcULqSLzRL3RMMhMTUMgSMmRMuEM8ENGRNLSNmUN2hOI"
}