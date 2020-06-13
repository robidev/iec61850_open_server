<?xml version="1.0" encoding="UTF-8"?>
<SCL version="2007" revision="A" xmlns="http://www.iec.ch/61850/2003/SCL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.iec.ch/61850/2003/SCL
schema/SCL.xsd" xmlns:ext="http://www.private.org">
  <Header id="proto" nameStructure="IEDName"/>
	<Substation name="S12" desc="Baden">
		<VoltageLevel name="D1">
			<PowerTransformer name="T1" type="PTR">
				<TransformerWinding name="W1" type="PTW">
					<Terminal connectivityNode="S12/D1/Q1/L1" substationName="S12" voltageLevelName="D1" bayName="Q1" cNodeName="L1"/>
				</TransformerWinding>
				<TransformerWinding name="W2" type="PTW">
					<Terminal connectivityNode="S12/E1/Q1/L3" substationName="S12" voltageLevelName="E1" bayName="Q1" cNodeName="L3"/>
				</TransformerWinding>
			</PowerTransformer>
			<Voltage multiplier="k" unit="V">220</Voltage>
			<Bay name="Q1">
        <ConductingEquipment name="external" type="IFL">
          <Terminal connectivityNode="S12/D1/Q1/L0" substationName="S12" voltageLevelName="D1" bayName="Q1" cNodeName="L0"/>
        </ConductingEquipment>
				<ConductingEquipment name="I1" type="CTR">
          <Terminal connectivityNode="S12/D1/Q1/L1" substationName="S12" voltageLevelName="D1" bayName="Q1" cNodeName="L1"/>
          <Terminal connectivityNode="S12/D1/Q1/L0" substationName="S12" voltageLevelName="D1" bayName="Q1" cNodeName="L0"/>
					<SubEquipment name="R" phase="A">
						<LNode lnClass="TCTR" iedName="IED3_SMV" ldInst="MUnn" lnInst="1"/>
					</SubEquipment>
					<SubEquipment name="S" phase="B">
						<LNode lnClass="TCTR" iedName="IED3_SMV" ldInst="MUnn" lnInst="2"/>
					</SubEquipment>
					<SubEquipment name="T" phase="C">
						<LNode lnClass="TCTR" iedName="IED3_SMV" ldInst="MUnn" lnInst="3"/>
					</SubEquipment>
					<SubEquipment name="I0" phase="N">
						<LNode lnClass="TCTR" iedName="IED3_SMV" ldInst="MUnn" lnInst="4"/>
					</SubEquipment>
        </ConductingEquipment>
				<ConnectivityNode name="L1" pathName="S12/D1/Q1/L1"/>
			</Bay>
		</VoltageLevel>
		<VoltageLevel name="E1">
			<Voltage multiplier="k" unit="V">132</Voltage>
			<Bay name="Q1">
				<ConductingEquipment name="QA1" type="CBR">
					<LNode lnInst="1" lnClass="XCBR" ldInst="GenericIO" iedName="IED1_XCBR"/>
					<Terminal connectivityNode="S12/E1/Q1/L1" substationName="S12" voltageLevelName="E1" bayName="Q1" cNodeName="L1"/>
					<Terminal connectivityNode="S12/E1/Q1/L2" substationName="S12" voltageLevelName="E1" bayName="Q1" cNodeName="L2"/>
				</ConductingEquipment>
				<ConductingEquipment name="QB1" type="DIS">
          <LNode lnInst="1" lnClass="XSWI" ldInst="GenericIO" iedName="IED1_XCBR"/>
					<Terminal connectivityNode="S12/E1/W1/BB1" substationName="S12" voltageLevelName="E1" bayName="W1" cNodeName="BB1"/>
					<Terminal connectivityNode="S12/E1/Q1/L1" substationName="S12" voltageLevelName="E1" bayName="Q1" cNodeName="L1"/>
				</ConductingEquipment>
				<ConductingEquipment name="U1" type="VTR">
					<Terminal connectivityNode="S12/E1/Q1/L2" substationName="S12" voltageLevelName="E1" bayName="Q1" cNodeName="L2"/>
					<SubEquipment name="A" phase="A">
						<LNode lnClass="TVTR" iedName="IED3_SMV" ldInst="MUnn" lnInst="1" desc="VT phase L1"/>
          </SubEquipment>
          <SubEquipment name="B" phase="B">
						<LNode lnClass="TVTR" iedName="IED3_SMV" ldInst="MUnn" lnInst="2" desc="VT phase L2"/>
          </SubEquipment>
          <SubEquipment name="C" phase="C">
						<LNode lnClass="TVTR" iedName="IED3_SMV" ldInst="MUnn" lnInst="3" desc="VT phase L3"/>
					</SubEquipment>
				</ConductingEquipment>
				<ConductingEquipment name="I1" type="CTR">
					<Terminal connectivityNode="S12/E1/Q1/L2" substationName="S12" voltageLevelName="E1" bayName="Q1" cNodeName="L2"/>
					<Terminal connectivityNode="S12/E1/Q1/L3" substationName="S12" voltageLevelName="E1" bayName="Q1" cNodeName="L3"/>
				</ConductingEquipment>
				<ConnectivityNode name="L1" pathName="S12/E1/Q1/L1"/>
				<ConnectivityNode name="L2" pathName="S12/E1/Q1/L2"/>
				<ConnectivityNode name="L3" pathName="S12/E1/Q1/L3"/>
      </Bay>
      <Bay name="W1">
				<ConnectivityNode name="BB1" pathName="S12/E1/W1/BB1" ext:type="load" ext:rload="5500"/>
			</Bay>
		</VoltageLevel>
	</Substation>

  <Communication>
    <SubNetwork name="subnetwork1" type="8-MMS">
      <ConnectedAP iedName="IED1_XCBR" apName="accessPoint1">
        <Address>
          <P type="IP">10.0.0.2</P>
          <P type="IP-SUBNET">255.255.255.0</P>
          <P type="IP-GATEWAY">10.0.0.1</P>
          <P type="OSI-TSEL">0001</P>
          <P type="OSI-PSEL">00000001</P>
          <P type="OSI-SSEL">0001</P>
        </Address>
        <GSE ldInst="GenericIO" cbName="gcbEvents">
           <Address>
                <P type="VLAN-ID">1</P>
                <P type="VLAN-PRIORITY">4</P>
                <P type="MAC-Address">01-0c-cd-04-00-01</P>
                <P type="APPID">1000</P>
           </Address>
	    </GSE>
      </ConnectedAP>
      <ConnectedAP iedName="IED2_PTOC" apName="accessPoint2">
        <Address>
          <P type="IP">10.0.0.3</P>
          <P type="IP-SUBNET">255.255.255.0</P>
          <P type="IP-GATEWAY">10.0.0.1</P>
          <P type="OSI-TSEL">0001</P>
          <P type="OSI-PSEL">00000001</P>
          <P type="OSI-SSEL">0001</P>
        </Address>
        <GSE ldInst="GenericIO" cbName="gcbEvents">
           <Address>
                <P type="VLAN-ID">1</P>
                <P type="VLAN-PRIORITY">4</P>
                <P type="MAC-Address">01-0c-cd-01-00-02</P>
                <P type="APPID">1002</P>
           </Address>
	    </GSE>
      </ConnectedAP>
      <ConnectedAP iedName="IED3_SMV" apName="accessPoint3">
        <Address>
          <P type="IP">10.0.0.4</P>
          <P type="IP-SUBNET">255.255.255.0</P>
          <P type="IP-GATEWAY">10.0.0.1</P>
          <P type="OSI-TSEL">0001</P>
          <P type="OSI-PSEL">00000001</P>
          <P type="OSI-SSEL">0001</P>
        </Address>
        <SMV ldInst="MUnn" cbName="MSVCB01">
	        <Address>
		        <P type="VLAN-ID">1</P>
		        <P type="VLAN-PRIORITY">4</P>
		        <P type="MAC-Address">01-0c-cd-01-00-01</P>
		        <P type="APPID">4000</P>
	        </Address>
        </SMV>
      </ConnectedAP>
    </SubNetwork>
  </Communication>

  <IED name="IED1_XCBR">
    <Services>
      <DynAssociation />
      <GetDirectory />
      <GetDataObjectDefinition />
      <GetDataSetValue />
      <DataSetDirectory />
      <ReadWrite />
      <GetCBValues />
      <ConfLNs fixPrefix="true" fixLnInst="true" />
      <GOOSE max="5" />
      <GSSE max="5" />
      <FileHandling />
      <GSEDir />
      <TimerActivatedControl />
    </Services>
    <AccessPoint name="accessPoint1">
      <Server>
        <Authentication />
        <LDevice inst="GenericIO">
          <LN0 lnClass="LLN0" lnType="LLN01" inst="">
          	<DataSet name="Events" desc="Events">
              <FCDA ldInst="GenericIO" lnClass="XCBR" fc="ST" lnInst="1" doName="Pos" daName="stVal" />
            </DataSet>
            
            <GSEControl appID="events" name="gcbEvents" type="GOOSE" datSet="Events" confRev="2" /> 
          </LN0>
          <LN lnClass="LPHD" lnType="LPHD1" inst="1" prefix="" />
          <LN lnClass="XCBR" lnType="XCBR1" inst="1" prefix="">
            <Inputs>
              <ExtRef intAddr="Tr" desc="Trip" iedName="IED2_PTOC" ldInst="GenericIO" lnClass="PTRC" lnInst="1" doName="Tr" daName="general" serviceType="GOOSE" srcLDInst="GenericIO" srcLNClass="LLN0" srcCBName="GoCB" />
            </Inputs>
          </LN>
          <LN lnClass="CSWI" lnType="CSWIa" inst="1" prefix="">
            <Inputs>
              <ExtRef intAddr="xcbr_stval" desc="xcbr_status" iedName="IED1_XCBR" ldInst="GenericIO" lnClass="XCBR" lnInst="1" doName="Pos" daName="stVal" serviceType="Poll" />
            </Inputs>
          </LN>
          <LN lnClass="XSWI" lnType="XSWI1" inst="2" prefix="">
            <DOI name="SwTyp">
              <DAI name="stVal">
                <Val>Disconnector</Val>
              </DAI>
            </DOI>
            <Inputs>
              <ExtRef intAddr="Tr" desc="Operate" iedName="IED1_XCBR" ldInst="GenericIO" lnClass="CSWI" lnInst="2" doName="Pos" daName="opOk" serviceType="Poll" />
            </Inputs>
          </LN>
          <LN lnClass="CSWI" lnType="CSWIa" inst="2" prefix="">
            <Inputs>
              <ExtRef intAddr="xcbr_stval" desc="xcbr_status" iedName="IED1_XCBR" ldInst="GenericIO" lnClass="XSWI" lnInst="2" doName="Pos" daName="stVal" serviceType="Poll" />
            </Inputs>
          </LN>
        </LDevice>
      </Server>
    </AccessPoint>
  </IED>
  <IED name="IED2_PTOC">
    <Services>
      <DynAssociation />
      <GetDirectory />
      <GetDataObjectDefinition />
      <GetDataSetValue />
      <DataSetDirectory />
      <ReadWrite />
      <GetCBValues />
      <ConfLNs fixPrefix="true" fixLnInst="true" />
      <GOOSE max="5" />
      <GSSE max="5" />
      <FileHandling />
      <GSEDir />
      <TimerActivatedControl />
    </Services>
    <AccessPoint name="accessPoint2">
      <Server>
        <Authentication />
        <LDevice inst="GenericIO">
          <LN0 lnClass="LLN0" lnType="LLN01" inst="">
          	<DataSet name="Events" desc="Events">
              <FCDA ldInst="GenericIO" lnClass="GGIO" fc="ST" lnInst="1" doName="SPCSO1" daName="stVal" />
              <FCDA ldInst="GenericIO" lnClass="PTRC" fc="ST" lnInst="1" doName="Tr" daName="general" />
            </DataSet>
            
            <GSEControl appID="events" name="gcbEvents" type="GOOSE" datSet="Events" confRev="2"  /> 
          </LN0>
          <LN lnClass="LPHD" lnType="LPHD1" inst="1" prefix="" />
          <LN lnClass="PTOC" lnType="PTOC1" inst="1" prefix="" >
            <DOI name="TmACrv">
              <DAI name="setCharact">
                <Val>ANSI Definite Time (Default)</Val>
              </DAI>
              <DAI name="setParA">
                <Val>1</Val>
              </DAI>
              <DAI name="setParB">
                <Val>2</Val>
              </DAI>
            </DOI>
            <Inputs>
              <ExtRef intAddr="Amp1" desc="sample_a1" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="1" doName="Amp" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp2" desc="sample_a2" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="2" doName="Amp" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp3" desc="sample_a3" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="3" doName="Amp" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp4" desc="sample_a4" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="4" doName="Amp" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol1" desc="sample_v1" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="1" doName="Vol" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol2" desc="sample_v2" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="2" doName="Vol" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol3" desc="sample_v3" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="3" doName="Vol" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol4" desc="sample_v4" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="4" doName="Vol" serviceType="SMV" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />

              <ExtRef intAddr="xcbr_stval" desc="xcbr_status" iedName="IED1_XCBR" ldInst="GenericIO" lnClass="XCBR" lnInst="1" doName="Pos" daName="stVal" serviceType="GOOSE" srcLDInst="GenericIO" srcLNClass="LLN0" srcCBName="GoCB" />
            </Inputs>
          </LN>
          <LN lnClass="PTRC" lnType="PTRC1" inst="1" prefix="" >
            <Inputs>
              <ExtRef intAddr="PTOC_Op" desc="PTOC_trip" iedName="IED2_PTOC" ldInst="GenericIO" lnClass="PTOC" lnInst="1" doName="Op" daName="general" serviceType="Poll" />
              <ExtRef intAddr="xcbr_stval" desc="xcbr_status" iedName="IED1_XCBR" ldInst="GenericIO" lnClass="XCBR" lnInst="1" doName="Pos" daName="stVal" serviceType="GOOSE" srcLDInst="GenericIO" srcLNClass="LLN0" srcCBName="GoCB" />
            </Inputs>
          </LN>
          <LN lnClass="GGIO" lnType="GGIO1" inst="1" prefix="">
            <DOI name="Mod">
              <DAI name="ctlModel">
                <Val>status-only</Val>
              </DAI>
            </DOI>
            <DOI name="SPCSO1">
              <DAI name="ctlModel">
                <Val>direct-with-normal-security</Val>
              </DAI>
            </DOI>
            <DOI name="SPCSO2">
              <DAI name="ctlModel">
                <Val>direct-with-normal-security</Val>
              </DAI>
            </DOI>
            <DOI name="SPCSO3">
              <DAI name="ctlModel">
                <Val>direct-with-normal-security</Val>
              </DAI>
            </DOI>
            <DOI name="SPCSO4">
              <DAI name="ctlModel">
                <Val>direct-with-normal-security</Val>
              </DAI>
            </DOI>
          </LN>
        </LDevice>
      </Server>
    </AccessPoint>
  </IED>
	<IED name="IED3_SMV">
		<AccessPoint name="accessPoint3">
			<Server>
				<Authentication />
				<LDevice inst="MUnn">
					<LN0 lnType="9-2LELLN0" lnClass="LLN0" inst="">
						<DataSet name="PhsMeas1">

							<FCDA ldInst="MUnn" lnClass="TCTR" lnInst="1" fc="MX" doName="Amp" />
							<FCDA ldInst="MUnn" lnClass="TCTR" lnInst="2" fc="MX"	doName="Amp" />
							<FCDA ldInst="MUnn" lnClass="TCTR" lnInst="3" fc="MX" doName="Amp" />
							<FCDA ldInst="MUnn" lnClass="TCTR" lnInst="4" fc="MX"	doName="Amp" />
							<FCDA ldInst="MUnn" lnClass="TVTR" lnInst="1" fc="MX"	doName="Vol" />
							<FCDA ldInst="MUnn" lnClass="TVTR" lnInst="2" fc="MX"	doName="Vol" />
							<FCDA ldInst="MUnn" lnClass="TVTR" lnInst="3" fc="MX"	doName="Vol" />
							<FCDA ldInst="MUnn" lnClass="TVTR" lnInst="4" fc="MX"	doName="Vol" />

						</DataSet>
						<SampledValueControl name="MSVCB01" datSet="PhsMeas1"
							smvID="xxxxMUnn01" smpRate="80" nofASDU="1" confRev="1">

							<SmvOpts refreshTime="false" sampleSynchronized="true"
								security="false" />
						</SampledValueControl>
					</LN0>

					<LN lnType="9-2LETCTR" lnClass="TCTR" inst="1" />
					<LN lnType="9-2LETCTR" lnClass="TCTR" inst="2" />
					<LN lnType="9-2LETCTR" lnClass="TCTR" inst="3" />
					<LN lnType="9-2LETCTR" lnClass="TCTR" inst="4" />

					<LN lnType="9-2LETVTR" lnClass="TVTR" inst="1" />
					<LN lnType="9-2LETVTR" lnClass="TVTR" inst="2" />
					<LN lnType="9-2LETVTR" lnClass="TVTR" inst="3" />
					<LN lnType="9-2LETVTR" lnClass="TVTR" inst="4" />

          <LN lnType="MMXUa" lnClass="MMXU" inst="1" >
            <Inputs>
              <ExtRef intAddr="Amp1" desc="sample_a1" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="1" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp2" desc="sample_a2" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="2" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp3" desc="sample_a3" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="3" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp4" desc="sample_a4" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="4" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol1" desc="sample_v1" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="1" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol2" desc="sample_v2" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="2" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol3" desc="sample_v3" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="3" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol4" desc="sample_v4" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="4" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
            </Inputs>
          </LN>
	        <LN lnType="MMXUa" lnClass="MMXU" inst="2" >
            <Inputs>
              <ExtRef intAddr="Amp1" desc="sample_a1" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="1" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp2" desc="sample_a2" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="2" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp3" desc="sample_a3" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="3" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Amp4" desc="sample_a4" iedName="IED3_SMV" ldInst="MUnn" lnClass="TCTR" lnInst="4" doName="Amp" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol1" desc="sample_v1" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="1" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol2" desc="sample_v2" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="2" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol3" desc="sample_v3" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="3" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
              <ExtRef intAddr="Vol4" desc="sample_v4" iedName="IED3_SMV" ldInst="MUnn" lnClass="TVTR" lnInst="4" doName="Vol" daName="instMag.i" serviceType="Poll" srcLDInst="MUnn" srcLNClass="LLN0" srcCBName="MSVCB01" />
            </Inputs>
          </LN>

				</LDevice>
			</Server>
		</AccessPoint>
	</IED>
  <DataTypeTemplates>

	<LNodeType id="9-2LELLN0" lnClass="LLN0">
		<DO name="Mod" type="9-2LEINC" />
	</LNodeType>

	<LNodeType id="9-2LETCTR" lnClass="TCTR">
		<DO name="Amp" type="9-2LESAVAmp" />
	</LNodeType>

	<LNodeType id="9-2LETVTR" lnClass="TVTR">
		<DO name="Vol" type="9-2LESAVVol" />
	</LNodeType>

    <LNodeType id="LLN01" lnClass="LLN0">
      <DO name="Mod" type="INC_1_Mod" />
      <DO name="Beh" type="INS_1_Beh" />
      <DO name="Health" type="INS_1_Beh" />
      <DO name="NamPlt" type="LPL_1_NamPlt" />
    </LNodeType>
    <LNodeType id="LPHD1" lnClass="LPHD">
      <DO name="PhyNam" type="DPL_1_PhyNam" />
      <DO name="PhyHealth" type="INS_1_Beh" />
      <DO name="Proxy" type="SPS_1_Proxy" />
    </LNodeType>

    <LNodeType id="PTRC1" lnClass="PTRC">
      <DO name="Mod" type="INC_2_Mod" />
      <DO name="Beh" type="INS_1_Beh" />
      <DO name="Health" type="INS_1_Beh" />
      <DO name="NamPlt" type="LPL_2_NamPlt" />
      <DO name="Op" type="ACT" />
      <DO name="Tr" type="ACT" />
    </LNodeType>

    <LNodeType id="PTOC1" lnClass="PTOC">
      <DO name="Mod" type="INC_2_Mod" />
      <DO name="Beh" type="INS_1_Beh" />
      <DO name="Health" type="INS_1_Beh" />
      <DO name="NamPlt" type="LPL_2_NamPlt" />
      <DO name="Str" type="ACD" />
      <DO name="Op" type="ACT" />
      <DO name="TmACrv" type="CURVE" />
    </LNodeType>

    <LNodeType id="XCBR1" lnClass="XCBR" desc="Circuit breaker">
      <DO name="Mod" type="INC_2_Mod" />
      <DO name="Beh" type="INS_1_Beh" />
      <DO name="Health" type="INS_1_Beh" />
      <DO name="NamPlt" type="LPL_2_NamPlt" />
      <DO name="Loc" type="SPC_1_SPCSO1" />
      <DO name="OpCnt" type="INS_1_Beh" />
      <DO name="Pos" type="DPC" />
      <DO name="BlkOpn" type="SPC_1_SPCSO1" />
      <DO name="BlkCls" type="SPC_1_SPCSO1" />
    </LNodeType>

    <LNodeType id="XSWI1" lnClass="XSWI" desc="Switch">
      <DO name="Mod" type="INC_2_Mod" />
      <DO name="Beh" type="INS_1_Beh" />
      <DO name="Health" type="INS_1_Beh" />
      <DO name="NamPlt" type="LPL_2_NamPlt" />
      <DO name="Loc" type="SPC_1_SPCSO1" />
      <DO name="OpCnt" type="INS_1_Beh" />
      <DO name="SwTyp" type="ENS" />
      <DO name="Pos" type="DPC" />
      <DO name="BlkOpn" type="SPC_1_SPCSO1" />
      <DO name="BlkCls" type="SPC_1_SPCSO1" />
    </LNodeType>

    <LNodeType id="CSWIa" lnClass="CSWI" desc="Controlable switch">
			<DO name="Mod" type="INC_2_Mod"/>
			<DO name="Beh" type="INS_1_Beh"/>
			<DO name="Health" type="INS_1_Beh"/>
			<DO name="NamPlt" type="LPL_2_NamPlt"/>
			<DO name="Pos" type="DPC_CO"/>
		</LNodeType>

		<LNodeType id="MMXUa" lnClass="MMXU">
			<DO name="Mod" type="INC_2_Mod"/>
			<DO name="Beh" type="INS_1_Beh"/>
			<DO name="Health" type="INS_1_Beh"/>
			<DO name="NamPlt" type="LPL_2_NamPlt"/>
			<DO name="AvAPhs" type="myMV"/>
			<DO name="AvPhVPhs" type="myMV"/>
      <DO name="MaxAPhs" type="myMV"/>
			<DO name="MaxPhVPhs" type="myMV"/>
      <DO name="MinAPhs" type="myMV"/>
			<DO name="MinPhVPhs" type="myMV"/>
		</LNodeType>

    <LNodeType id="GGIO1" lnClass="GGIO">
      <DO name="Mod" type="INC_2_Mod" />
      <DO name="Beh" type="INS_1_Beh" />
      <DO name="Health" type="INS_1_Beh" />
      <DO name="NamPlt" type="LPL_2_NamPlt" />
      <DO name="AnIn1" type="MV_1_AnIn1" />
      <DO name="AnIn2" type="MV_1_AnIn1" />
      <DO name="AnIn3" type="MV_1_AnIn1" />
      <DO name="AnIn4" type="MV_1_AnIn1" />
      <DO name="SPCSO1" type="SPC_2_SPCSO1" />
      <DO name="SPCSO2" type="SPC_1_SPCSO2" />
      <DO name="SPCSO3" type="SPC_1_SPCSO3" />
      <DO name="SPCSO4" type="SPC_1_SPCSO1" />
      <DO name="Ind1" type="SPS_1_Proxy" />
      <DO name="Ind2" type="SPS_1_Proxy" />
      <DO name="Ind3" type="SPS_1_Proxy" />
      <DO name="Ind4" type="SPS_1_Proxy" />
    </LNodeType>

  <DOType id="CURVE" cdc="CURVE">
    <DA name="setCharact" fc="SP" dchg="true" bType="Enum" type="setCharact_1"/>
    <DA name="setParA" fc="SP" dchg="true" bType="FLOAT32"/>
    <DA name="setParB" fc="SP" dchg="true" bType="FLOAT32"/>
    <DA name="setParC" fc="SP" dchg="true" bType="FLOAT32"/>
    <DA name="setParD" fc="SP" dchg="true" bType="FLOAT32"/>
    <DA name="setParE" fc="SP" dchg="true" bType="FLOAT32"/>
    <DA name="setParF" fc="SP" dchg="true" bType="FLOAT32"/>
  </DOType>

  <DOType id="myMV" cdc="MV">
    <DA name="mag" fc="MX" dchg="true" bType="Struct" type="AnalogueValue_1"/>
    <DA name="q" fc="MX" qchg="true" bType="Quality"/>
    <DA name="t" fc="MX" bType="Timestamp"/>
    <DA name="sVC" fc="CF" dchg="true" bType="Struct" type="ScaledValueConfig"/>
  </DOType>
  <DOType cdc="DPC" id="DPC" desc="Controllable double point CDC.">
    <DA name="stVal" bType="Dbpos" fc="ST" dchg="true" desc="intermediate-state | off | on | bad-state" />
    <DA name="q" bType="Quality" fc="ST" qchg="true" desc="Quality of the data value: 'stVal'." />
    <DA name="t" bType="Timestamp" fc="ST" desc="Timestamp of the last change in one of the attributes representing the data value ('stVal') or the data quality ('q'), i.e., those which have 'dchg' or 'qchg'." />
  </DOType>
  <DOType cdc="ENS" id="ENS" desc="Enumerated status">
    <DA name="stVal" bType="Enum" type="SwTyp_Enum" fc="ST" dchg="true" desc="" />
    <DA name="q" bType="Quality" fc="ST" qchg="true" desc="Quality of the data value: 'stVal'." />
    <DA name="t" bType="Timestamp" fc="ST" desc="Timestamp of the last change in one of the attributes representing the data value ('stVal') or the data quality ('q'), i.e., those which have 'dchg' or 'qchg'." />
  </DOType>
  <DOType cdc="DPC" id="DPC_CO" desc="Controllable double point CDC.">
    <DA name="stVal" bType="Dbpos" fc="ST" dchg="true" desc="intermediate-state | off | on | bad-state" />
    <DA name="q" bType="Quality" fc="ST" qchg="true" desc="Quality of the data value: 'stVal'." />
    <DA name="t" bType="Timestamp" fc="ST" desc="Timestamp of the last change in one of the attributes representing the data value ('stVal') or the data quality ('q'), i.e., those which have 'dchg' or 'qchg'." />
    <DA name="opOk" bType="BOOLEAN" fc="OR" dchg="true" />
    <DA name="ctlModel" fc="CF" bType="Enum" type="CtlModels"/>
    <DA name="Oper" fc="CO" bType="Struct" type="DPCOperate_1"/>
    <DA name="SBOw" fc="CO" bType="Struct" type="DPCOperate_1"/>
    <DA name="Cancel" fc="CO" bType="Struct" type="myCancel"/>
  </DOType>
  <DOType id="ACD" cdc="ACD">
    <DA name="general" fc="ST" dchg="true" bType="BOOLEAN" />
    <DA name="dirGeneral" fc="ST" dchg="true" bType="Enum" type="ACDdir" />
    <DA name="q" fc="ST" qchg="true" bType="Quality" />
    <DA name="t" fc="ST" bType="Timestamp" />
  </DOType>
  <DOType id="ACT" cdc="ACT">
    <DA name="general" fc="ST" dchg="true" bType="BOOLEAN" />
    <DA name="q" fc="ST" qchg="true" bType="Quality" />
    <DA name="t" fc="ST" bType="Timestamp" />
  </DOType>

	<DOType id="9-2LESAVAmp" cdc="SAV">
		<DA name="instMag" bType="Struct" type="9-2LEAV" fc="MX" />
		<DA name="q" bType="Quality" fc="MX" />
		<DA name="sVC" bType="Struct" type="9-2LEsVCAmp" fc="CF" />
	</DOType>

	<DOType id="9-2LESAVVol" cdc="SAV">
		<DA name="instMag" bType="Struct" type="9-2LEAV" fc="MX" />
		<DA name="q" bType="Quality" fc="MX" />
		<DA name="sVC" bType="Struct" type="9-2LEsVCVol" fc="CF" />
	</DOType>

	<DOType id="9-2LEINC" cdc="INC">
		<DA name="stVal" fc="ST" bType="INT32" dchg="true" />
		<DA name="q" fc="ST" bType="Quality" dchg="true" />
		<DA name="t" fc="ST" bType="Timestamp" dchg="true" />
	</DOType>

    <DOType id="INC_1_Mod" cdc="INC">
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="t" bType="Timestamp" fc="ST" />
      <DA name="ctlModel" type="CtlModels" bType="Enum" fc="CF" />
    </DOType>
    <DOType id="INS_1_Beh" cdc="INS">
      <DA name="stVal" bType="INT32" fc="ST" dchg="true" />
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="t" bType="Timestamp" fc="ST" />
    </DOType>
    <DOType id="LPL_1_NamPlt" cdc="LPL">
      <DA name="vendor" bType="VisString255" fc="DC" />
      <DA name="swRev" bType="VisString255" fc="DC" />
      <DA name="d" bType="VisString255" fc="DC" />
      <DA name="configRev" bType="VisString255" fc="DC" />
      <DA name="ldNs" bType="VisString255" fc="EX" />
    </DOType>
    <DOType id="DPL_1_PhyNam" cdc="DPL">
      <DA name="vendor" bType="VisString255" fc="DC" />
    </DOType>
    <DOType id="SPS_1_Proxy" cdc="SPS">
      <DA name="stVal" bType="BOOLEAN" fc="ST" dchg="true" />
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="t" bType="Timestamp" fc="ST" />
    </DOType>
    <DOType id="LPL_2_NamPlt" cdc="LPL">
      <DA name="vendor" bType="VisString255" fc="DC" />
      <DA name="swRev" bType="VisString255" fc="DC" />
      <DA name="d" bType="VisString255" fc="DC" />
    </DOType>
    <DOType id="MV_1_AnIn1" cdc="MV">
      <DA name="mag" type="AnalogueValue_1" bType="Struct" fc="MX" dchg="true" />
      <DA name="q" bType="Quality" fc="MX" qchg="true" />
      <DA name="t" bType="Timestamp" fc="MX" />
    </DOType>
    <DOType id="SPC_1_SPCSO1" cdc="SPC">
      <DA name="stVal" bType="BOOLEAN" fc="ST" dchg="true" />
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="Oper" type="SPCOperate_1" bType="Struct" fc="CO" />
      <DA name="ctlModel" type="CtlModels" bType="Enum" fc="CF" />
      <DA name="t" bType="Timestamp" fc="ST" />
    </DOType>
    <DOType id="INC_2_Mod" cdc="INC">
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="t" bType="Timestamp" fc="ST" />
      <DA name="ctlModel" type="CtlModels" bType="Enum" fc="CF" />
    </DOType>
    <DOType id="SPC_2_SPCSO1" cdc="SPC">
      <DA name="stVal" bType="BOOLEAN" fc="ST" dchg="true" />
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="Oper" type="SPCOperate_1" bType="Struct" fc="CO" />
      <DA name="ctlModel" type="CtlModels" bType="Enum" fc="CF" />
      <DA name="t" bType="Timestamp" fc="ST" />
    </DOType>
    <DOType id="SPC_1_SPCSO2" cdc="SPC">
      <DA name="stVal" bType="BOOLEAN" fc="ST" dchg="true" />
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="Oper" type="SPCOperate_1" bType="Struct" fc="CO" />
      <DA name="ctlModel" type="CtlModels" bType="Enum" fc="CF" />
      <DA name="t" bType="Timestamp" fc="ST" />
    </DOType>
    <DOType id="SPC_1_SPCSO3" cdc="SPC">
      <DA name="stVal" bType="BOOLEAN" fc="ST" dchg="true" />
      <DA name="q" bType="Quality" fc="ST" qchg="true" />
      <DA name="Oper" type="SPCOperate_1" bType="Struct" fc="CO" />
      <DA name="ctlModel" type="CtlModels" bType="Enum" fc="CF" />
      <DA name="t" bType="Timestamp" fc="ST" />
    </DOType>

		<DAType id="ScaledValueConfig">
			<BDA name="scaleFactor" bType="FLOAT32"/>
			<BDA name="offset" bType="FLOAT32"/>
		</DAType>
	<DAType id="9-2LEAV">
		<BDA name="i" bType="INT32" />
	</DAType>
	<DAType id="9-2LEsVCAmp">
		<BDA name="scaleFactor" bType="FLOAT32">
			<Val>0.001</Val>
		</BDA>
		<BDA name="offset" bType="FLOAT32">
			<Val>0</Val>
		</BDA>
	</DAType>
	<DAType id="9-2LEsVCVol">
		<BDA name="scaleFactor" bType="FLOAT32">
			<Val>0.01</Val>
		</BDA>
		<BDA name="offset" bType="FLOAT32">
			<Val>0</Val>
		</BDA>
	</DAType>

    <DAType id="AnalogueValue_1">
      <BDA name="f" bType="FLOAT32" />
    </DAType>
    <DAType id="Originator_1">
      <BDA name="orCat" type="OrCat" bType="Enum" />
      <BDA name="orIdent" bType="Octet64" />
    </DAType>
    <DAType id="SPCOperate_1">
      <BDA name="ctlVal" bType="BOOLEAN" />
      <BDA name="origin" type="Originator_1" bType="Struct" />
      <BDA name="ctlNum" bType="INT8U" />
      <BDA name="T" bType="Timestamp" />
      <BDA name="Test" bType="BOOLEAN" />
      <BDA name="Check" bType="Check" />
    </DAType>
    <DAType id="DPCOperate_1">
      <BDA name="ctlVal" bType="BOOLEAN" />
      <BDA name="origin" type="Originator_1" bType="Struct" />
      <BDA name="ctlNum" bType="INT8U" />
      <BDA name="T" bType="Timestamp" />
      <BDA name="Test" bType="BOOLEAN" />
      <BDA name="Check" bType="Check" />
    </DAType>
    <DAType id="myCancel">
			<BDA name="ctlVal" bType="BOOLEAN"/>
			<BDA name="origin" bType="Struct" type="Originator_1"/>
			<BDA name="ctlNum" bType="INT8U"/>
			<BDA name="T" bType="Timestamp"/>
			<BDA name="Test" bType="BOOLEAN"/>
		</DAType>
    <EnumType id="CtlModels">
      <EnumVal ord="0">status-only</EnumVal>
      <EnumVal ord="1">direct-with-normal-security</EnumVal>
      <EnumVal ord="2">sbo-with-normal-security</EnumVal>
      <EnumVal ord="3">direct-with-enhanced-security</EnumVal>
      <EnumVal ord="4">sbo-with-enhanced-security</EnumVal>
    </EnumType>
    <EnumType id="OrCat">
      <EnumVal ord="0">not-supported</EnumVal>
      <EnumVal ord="1">bay-control</EnumVal>
      <EnumVal ord="2">station-control</EnumVal>
      <EnumVal ord="3">remote-control</EnumVal>
      <EnumVal ord="4">automatic-bay</EnumVal>
      <EnumVal ord="5">automatic-station</EnumVal>
      <EnumVal ord="6">automatic-remote</EnumVal>
      <EnumVal ord="7">maintenance</EnumVal>
      <EnumVal ord="8">process</EnumVal>
    </EnumType>
    <EnumType id="ACDdir">
      <EnumVal ord="0">unknown</EnumVal>
      <EnumVal ord="1">forward</EnumVal>
      <EnumVal ord="2">backward</EnumVal>
      <EnumVal ord="3">both</EnumVal>
    </EnumType>
    <EnumType id="setCharact_1">
      <EnumVal ord="0">unknown</EnumVal>
      <EnumVal ord="1">ANSI Extremely Inverse</EnumVal>
      <EnumVal ord="2">ANSI Very Inverse</EnumVal>
      <EnumVal ord="3">ANSI Normal Inverse</EnumVal>
      <EnumVal ord="4">ANSI Moderately Inverse</EnumVal>
      <EnumVal ord="5">ANSI Definite Time (Default)</EnumVal>
      <EnumVal ord="6">Long-Time Extremely Inverse</EnumVal>
      <EnumVal ord="7">Long-Time Very Inverse</EnumVal>
      <EnumVal ord="8">Long-Time Inverse</EnumVal>
      <EnumVal ord="9">IEC Normal Inverse</EnumVal>
      <EnumVal ord="10">IEC Very Inverse</EnumVal>
      <EnumVal ord="11">IEC Inverse</EnumVal>
      <EnumVal ord="12">IEC Extremely Inverse</EnumVal>
      <EnumVal ord="13">IEC Short-Time Inverse</EnumVal>
      <EnumVal ord="14">IEC Long-Time Inverse</EnumVal>
      <EnumVal ord="15">IEC Definite Time</EnumVal>
      <EnumVal ord="16">reserved</EnumVal>
      <EnumVal ord="17">Definable curve 1 based on formula [x=f(y,A,B,C,D, E, F)]</EnumVal>
    </EnumType>
    <EnumType id="SwTyp_Enum">
      <EnumVal ord="0">unknown</EnumVal>
      <EnumVal ord="1">Load break switch</EnumVal>
      <EnumVal ord="2">Disconnector</EnumVal>
      <EnumVal ord="3">Earthing switch</EnumVal>
      <EnumVal ord="4">High speed earthing switch</EnumVal>
    </EnumType>
  </DataTypeTemplates>
</SCL>
