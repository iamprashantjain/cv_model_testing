import streamlit as st
import pickle
import numpy as np
import pdb


def load_model():
		with open('saved_steps.pkl','rb') as file:
				data = pickle.load(file)

		return data


data = load_model()

model_loaded = data['model']
le_Model = data['le_Model']
le_Variant = data['le_Variant']
le_STATE_MAPPED = data['le_STATE_MAPPED']
le_Make = data['le_Make']


def show_predict_page():
		st.image('https://web.samil.in/wp-content/uploads/2020/01/Theme1/Desktop-T_1.png')
		st.title("Sold Amount Prediction")
		st.write("Select below information to predict.")

		model = (
			'2518TR', '3118HL', '4023', '2516HL', '3118', '4018', '2518',
			 '3116', '4923', '1112', '1613', '1616GOLD', '1618', 'GURU1111',
			 'GURU1211', 'TUSKERSUPER1616', 'ECOMET912', 'ALPSV4/38210WBViking',
			 'TUSKERSUPER2214/1S', '12MFESLFBSIV', '1616', '3121', '3518 BS6',
			 '912', 'ALPSV4/62', 'ECOMET1012', 'ECOMET1212', 'ECOMET1112',
			 '1618XP', 'U4023', '2516', 'BOSS1213LS', 'TAURUS2518H', 'U4923',
			 '1212', '1611', '1611COMET', 'BOSS913LS', 'TAURUS2516H',
			 'VIKINGALPSV4/186,222BUS', 'ALPSV4/88BSII', '1512',
			 'ALPSV4/51,BSII', '4921', '4019ILTT', 'VIKINGALPSV4/190', '2516XL',
			 'DOSTLE', '2214', 'TUSKERSUPER2214X', 'LynxSmart', '3718',
			 'TUSKERSUPER2516H', '4018TT', 'VIKINGALPSV4/170',
			 'VIKINGALPSV4/186', 'CG1613HBSIII', '1612', 'CT1613H/1BSII',
			 '3518U', '1613HCOMETGOLD', '3121H',
			 'ECOMET1214', 'LYNXSMART1310', '2518XL', '3118XP', '3518',
			 '3516TT', '3/10COMET', 'BOSS1113', 'ALPSV4/89Bus', 'AL4/89',
			 '1613COMETSUPER', '1616COMETCT', 'CARGO759', 'ALPSV1/40',
			 'U3718CABCHASSIS', '1214', 'PARTNER', 'ALPSV4/185210WBViking',
			 '1616XL', 'BOSS1212LE', '2516IL', 'CheetahALPSV4.187,BS-III',
			 'STAGALPSV3/73BUS', 'TUSKERSUPER2514H', '12M', '2513', '2513H/1',
			 'CARGO709', 'TUSKERSUPER2214', '4019', '4018H', 'CARGO909',
			 '1613COMETGOLD', '2518H', '3116H', 'DOSTLX', '1611COMETCT',
			 '2516/1TAURUS', '3516', 'Viking4/62,BSII', '2516H', 'IL3718',
			 '1613COMETCT', '1612COMET', '2214/1S', 'DOSTLS', 'DOST', '1214R',
			 '1617R', '2523', '3123', '1617', '4928TT', '2523R', '1617R(A/C)',
			 '914R', '3723R', '10.90SKYLINEFBV', '11.1', 'PRO5031',
			 '10.50SKYLINE', '10.75SKYLINEFBV', '10.95', '40.4', '60.25',
			 'PRO1080XP', 'PRO5025', 'PRO5035', 'PRO6025', 'SKYLINEPRO3008',
			 '10.50SKYLINEFBV', '11.10FBV', 'PRO5016', '10.90CRUISER', '35.31',
			 'HERCULES35.31', '10.50STARLINE', '10.75', '10.90SKYLINE', '10.6',
			 '20.15FBV', '30.25', 'MULTIX', '10.70CRUISERFBV', '10.8',
			 'PRO6037', '33.25GALAXY', 'SKYLINEPRO3009', '10.75STARLINE',
			 'PRO1114XP', '10.75SKYLINE', '30.25GALAXY', '3014',
			 '10.90STARLINE', 'PRO6031', 'PRO1049', 'MULTIXMX', 'TERRA25',
			 '10.55', '20.16', '3015', '10.75CRUISER', 'PRO3013', '15.16',
			 '20.15', 'TERRA16', 'PRO1110XP', '11.14', '10.7', '11.12',
			 'JUMBO20.16', '10.5', '10.59', '10.9', 'TRAVELLER', 'CITILINE',
			 'TRIP', 'SHAKTIMAN200', 'TRAVELLER26', 'TRAVELLER4020',
			 'TRAXTD2650F', 'COMMUTER', 'TRUMP15', 'TEMPOEXCEL', 'TRUMP40',
			 'KARGOKING', 'TEMPOTRAVELLER', 'CLA25.180', 'CLA40.220',
			 'CLA40.280', 'CLA25.220', '25.22', 'CLA31.220', 'CLA49.280',
			 'WINNER1.5XD', 'RTVFBV', 'WINNER1.8CNGBSIV', 'BLAZO55', 'TRUXO37',
			 'NAVISTARMN31', 'BLAZO25', 'BLAZO35', 'BLAZO49', 'TRACO35',
			 'BOLERO', 'IMPERIO', 'NAVISTARMN40', 'TRACO40', 'NAVISTARMN31FBT',
			 'TOURISTER', 'BLAZO31', 'BLAZO40', 'SUPRO', 'DI3150',
			 'MAXITRUCKCNG', 'DI3200', 'LOADKING', 'BOLEROMAXITRUCK',
			 'ALLWYNNISSAN', 'TOURISTEREXCELO', 'TOURISTERFBV', 'TRUXO25',
			 'MN31', 'JEETO', 'BLAZO37', 'SUPROLX8SEATER', 'CABKING', 'TRUXO31',
			 'MAXXIMOPLUS', 'TOURISTERCNG', 'BOLEROMAXITRUCKCNG',
			 'BOLEROCAMPER', 'NAVISTARMN25', 'GIO', 'SUPROMAXITRUCKT2BSIII',
			 'GENIO', 'MAXX', 'MAXICAB', 'MAXITRUCK', 'MAXXIMO', 'SUPERCARRY',
			 'PORTER700', 'PORTER1000', 'PORTER600', 'APEMINITRUCK',
			 'APETRUCKPLUS', 'APETRUCK', 'PALROADSTAR', 'LT134', 'DMAX',
			 'SAMRAT17', 'IS12T', 'SAMRATHD19XM', 'WT48AMBULANCE', 'T3500WV26',
			 'SUPERCNG', 'SARTAJWV26S', '4WDBT', 'SARTAJ', 'WT50LWB',
			 'SARTAJTC', 'PRESTIGE', 'T3500WT48', 'PREMIUM',
			 'PRESTIGESEMIDELUXETCIIIWT50LWBCNG', 'T3500', 'SAMRATZT54ELBW',
			 'SUPREME', 'COSMO', 'SUPERTC', 'ZT54', 'SAMRATZT54', 'SAMRAT',
			 'SUPER', 'LP1312', 'LP708', 'LP912AC', 'LPT1512', 'LPT1615',
			 'LPT2515', 'LPT2516', 'LPT2516TURBOSUPER', 'LPT709', 'LPT809',
			 'PRIMA4028S', 'SE1210', 'SE1613', 'SFC407', 'SIGNA4923', 'LPS4021',
			 '909', 'LP1512CUMMINS', 'LPO1610', 'LPO1616CUMMINS', 'LPT1010',
			 'LPT1412', 'LPT1613', 'LPT2515CUMMINS', 'LPT3118', 'LPT3718',
			 'LPT4223', 'LPT712', 'LPT909', 'LPT912', 'SFC608', 'SFC709',
			 'ULTRA1014', 'ULTRA814', 'LPS4023S', 'LP709MARCOPOLO', 'LPT2518',
			 'LPT2518TURBO', 'WINGERPRM', 'LP712AC', 'LP909MARCOPOLO',
			 'LPO1612CUMMINS', 'LPT1510', 'SE1510', '810EX2', 'ACE', 'SE1612',
			 'LP912MARCOPOLO', 'LPT407', 'ULTRA1012', 'LPO918GLOBUS20',
			 'LPT1109', 'LPT1112', 'XENONSUPERCNG', 'LP909', 'WINGER', '207',
			 'LPT2213', 'LP609', 'LP1510TURBO', 'LPT2518CUMMINS', 'LP1112',
			 'LPO1510TURBO', 'LPO1616GLOBUS', 'SFC410', 'LP912', 'SE1616',
			 'LPT3118CUMMINS', 'INTRAV10', 'LPS4923', 'STARBUS', 'LPT1412CRX',
			 'XENONXTCNG', 'SFC909', 'LP410', 'LPO1613TURBO', 'LP1210', '2515',
			 'LP709', 'XENONEX4X4', 'ACECNG', 'LPT2515TURBO', 'WINGERDLX',
			 'LPO1512CUMMINS', 'XENONCNG', 'LP712', 'LP712STAR', 'LPT2515EX',
			 'ACEZIPXL', 'ULTRA1518', 'XENONEXCNG', 'MEGAXL', 'LP1109',
			 'LPO1510', 'XENON', 'LPT1616', 'SE1613TURBO', 'LPS3518', 'ACEXL',
			 'LP1510', 'LPT1613TURBO', 'VENTURE', 'SUPERACEMINT', 'CITYRIDE',
			 'LP407', 'XENONRX', 'MAGIC', 'ACEDICOR', '207DIEX', 'VENTURECX',
			 'LPS3516', 'XENONEX', 'ACEBSIII', 'LPS4018', 'VENTUREEX',
			 'VENTUREGX', 'WINGERSTD', 'ACEBSII', 'ACEHTBSII', 'ACEMEGA',
			 'MAGICIRIS', 'MAGICHT', '207DI', 'ACEEX', 'ACEZIP', 'SUPERACE',
			 'ACEHT', 'DCM', '9400MULTIAXLE', 'B7R'
			 )
		
		variant = (
			'6X2CABCHASSISTRUCK', '8X2CABANDCHASSISTRUCK',
			 '4X2COMBINATIONTRUCK', '6X2CARGOTRUCK', '4X2TRUCKTRACTOR',
			 '6X2COWLCHASSISTRUCK', '8X2CARGOTRUCK', '6X2COMBINATIONTRUCK',
			 '8X4CARGOTRUCK', '4X4CARGOTRUCK', '4X2CONTAINERIZEDTRUCK',
			 '8X2FUELTANKTRUCK', '8X2FLATBEDTRUCK', '4X2CARGOTRUCK',
			 '4X2TANKERTRUCK', '4X2BUS', '4X2CONTAINERCHASSISTRUCK',
			 '8X2EDIBLEOILTANKTRUCK', '8X2CABCHASSISTRUCK',
			 '8X2CHEMICALTANKTRUCK', '4X2CABCHASSISTRUCK', '4X2FLATBEDTRUCK',
			 '4X2FUELTANKTRUCK', '6X2FUELTANKTRUCK', '6X2TANKERTRUCK',
			 '8X2WATERTANKTRUCK', '6X2CONTAINERIZEDTRUCK', '6X2TRUCKTRACTOR',
			 '4X2WATERTANKTRUCK', '8X2TANKERTRUCK', '6X4CABCHASSISTRUCK',
			 '6X2WATERTANKTRUCK', '4X2TANKER', '6X4COMBINATIONTRUCK',
			 '4X2MINIBUS', '10X2CABCHASSISTRUCK', '6X4CARGOTRUCK',
			 '8X2REEFERTRUCK', '6X4TRUCKTRACTOR', '10X2CARGOTRUCK',
			 '6X4CABANDCHASSISTRUCK', '6X2CABANDCHASSISTRUCK', '4X2PICKUP',
			 '6X2FLATBEDTRUCK', '8X2CONTAINERIZEDTRUCK', '4X2REEFERTRUCK',
			 '4X2CONTAENERTRUCK', '4X2SCHOOLBUS', '4X2MILKTANKTRUCK',
			 '6X2CONTAINERTRUCK', '8X2MILKTANKTRUCK', '4X2CABANDCHASSISTRUCK',
			 '4X2CREWCABPICKUP', '4X2CONTAINERTRUCK', '8X2TANKTRUCK',
			 '4X2INSULATEDTRUCK', '4X2AMBULANCE', '4X2DELIVERYVAN',
			 '4X2CARGOVAN', '4X4PICKUP', '4X2MOBILEBANKINGVAN',
			 '4X2FIREBRIGADES', '4X2TOWTRUCK', '8X2ASPHALTTANKTRUCK',
			 '10X2CEMENTBULKTRUCK', '4X2VACUUMTRUCK', '4X2BOOMTRUCK',
			 '4X2MINIWATERTANK', '10X2COWLCHASSISTRUCK', '8X2CEMENTBULKTRUCK',
			 '6X2CONTINERTRUCK', '4X2WATERTANKER', '6X2OILTANKER',
			 '6X2TANKTRUCK', '6X2TANKER', '4X2MINIBUSHARDTOP'
			 )
		
		state_mapped = (
			'Rajasthan', 'Punjab', 'Tamil Nadu', 'Gujarat', 'Kerala',
			 'Andhra Pradesh', 'Jharkhand', 'Uttar Pradesh', 'Maharashtra',
			 'Chhattisgarh', 'Nagaland', 'Karnataka', 'Telangana', 'Bihar',
			 'Himachal Pradesh', 'Haryana', 'Madhya Pradesh', '0',
			 'West Bengal', 'Puducherry','Jammu And Kashmir', 'Assam',
			 'Delhi', 'Uttarakhand'
			 )
		
		make = (
			'AMW', 'ASHOKLEYLAND', 'BHARATBENZ', 'EICHER', 'FORCE', 'FORCEMAN',
			 'HINDUSTAN', 'MAHINDRA', 'MARUTISUZUKI', 'PIAGGIO', 'PREMIER',
			 'SMLISUZU', 'SWARAJMAZDA', 'TATA', 'TOYOTA', 'VOLVO'
			 )
		

		mfy = (
			2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022
		)            


		mfy = st.selectbox('Manufacturing Year',mfy)  
		model = st.selectbox("Model", model)
		variant = st.selectbox("Variant",variant)
		state_mapped = st.selectbox("State",state_mapped)
		make = st.selectbox("Make",make)
		
		ok = st.button("Calculate Sold Amount")

		if ok:
			X = np.array([[mfy,model,variant,state_mapped,make]],dtype=object)
			X[:, 1] = le_Model.transform(X[:,1])
			X[:, 2] = le_Variant.transform(X[:,2])
			X[:, 3] = le_STATE_MAPPED.transform(X[:,3])
			X[:, 4] = le_Make.transform(X[:,4])
			

			sold_amt = model_loaded.predict(X)
			st.subheader(f"The Estimated Sold AMount is ₹{sold_amt[0]:.2f}")