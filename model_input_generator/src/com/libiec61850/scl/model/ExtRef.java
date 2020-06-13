package com.libiec61850.scl.model;

/*
 *  Copyright 2013 Michael Zillgith
 *
 *	This file is part of libIEC61850.
 *
 *	libIEC61850 is free software: you can redistribute it and/or modify
 *	it under the terms of the GNU General Public License as published by
 *	the Free Software Foundation, either version 3 of the License, or
 *	(at your option) any later version.
 *
 *	libIEC61850 is distributed in the hope that it will be useful,
 *	but WITHOUT ANY WARRANTY; without even the implied warranty of
 *	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *	GNU General Public License for more details.
 *
 *	You should have received a copy of the GNU General Public License
 *	along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
 *
 *	See COPYING file for the complete license text.
 */

import org.w3c.dom.Node;

import com.libiec61850.scl.ParserUtils;
import com.libiec61850.scl.SclParserException;

public class ExtRef {


	private String desc = null;
	
    private String iedName = null;
	private String ldInst = null;
	private String prefix = null;
	private String lnClass = null;
	private String lnInst = null;
	private String doName = null;
	private String daName = null;

	private String intAddr = null;
	private String serviceType = null;

	private String srcLDInst = null;
	private String srcPrefix = null;
	private String srcLNClass = null;
	private String srcLNInst = null;
	private String srcCBName = null;
	
	public ExtRef(Node extRefNode) throws SclParserException {

		this.desc = ParserUtils.parseAttribute(extRefNode, "desc");

		this.iedName = ParserUtils.parseAttribute(extRefNode, "iedName");
		this.ldInst = ParserUtils.parseAttribute(extRefNode, "ldInst");
		this.prefix = ParserUtils.parseAttribute(extRefNode, "prefix");	
		this.lnClass = ParserUtils.parseAttribute(extRefNode, "lnClass");
		this.lnInst= ParserUtils.parseAttribute(extRefNode, "lnInst");
		this.doName = ParserUtils.parseAttribute(extRefNode, "doName");
		this.daName = ParserUtils.parseAttribute(extRefNode, "daName");
		
    	this.intAddr = ParserUtils.parseAttribute(extRefNode, "intAddr");
		this.serviceType = ParserUtils.parseAttribute(extRefNode, "serviceType");

		this.srcLDInst = ParserUtils.parseAttribute(extRefNode, "srcLDInst");
		this.srcPrefix = ParserUtils.parseAttribute(extRefNode, "srcPrefix");
		this.srcLNClass = ParserUtils.parseAttribute(extRefNode, "srcLNClass");
		this.srcLNInst = ParserUtils.parseAttribute(extRefNode, "srcLNInst");
		this.srcCBName = ParserUtils.parseAttribute(extRefNode, "srcCBName");
	}

	public String getDesc() {
		return desc;
	}
	public String getIedName() {
		return iedName;
	}

	public String getLdInstance() {
		return ldInst;
	}

	public String getPrefix() {
        return prefix;
    }

	public String getLnClass() {
		return lnClass;
	}

	public String getLnInstance() {
		return lnInst;
	}

	public String getDoName() {
		return doName;
	}

	public String getDaName() {
		return daName;
	}
	
	public String getIntAddr() {
		return intAddr;
	}

	public String getServiceType() {
		return serviceType;
	}

	public String getSrcLdInstance() {
		return srcLDInst;
	}

	public String getSrcPrefix() {
        return srcPrefix;
    }

	public String getSrcLnClass() {
		return srcLNClass;
	}

	public String getSrcLnInstance() {
		return srcLNInst;
	}

	public String getSrcCBName() {
		return srcCBName;
	}

    @Override
	public String toString() {
		String string = "";

		if (iedName != null)
			string += iedName;
		
		if (ldInst != null)
			string += ldInst + "/";
		
		if (lnClass != null) {
		    
		    if (prefix != null)
		        string += prefix;
		    
			string += lnClass;
			if (lnInst == null)
				string += ".";
		}
		
		if (lnInst != null)
			string += lnInst + ".";
		
		if (doName != null)
			string += doName;
		
		if (daName != null)
			string += "." + daName;
		
		return string;
	}
	
	public String ExtRefToString() {
		String string = "";

		if (iedName != null)
			string += iedName;
		
		if (ldInst != null)
			string += ldInst;
		
		string += "/";
		
		if (lnClass != null) {
		    
		    if (prefix != null)
		        string += prefix;
		    
			string += lnClass;
			if (lnInst == null)
				string += ".";
		}
		
		if (lnInst != null)
			string += lnInst + ".";
		
		if (doName != null)
			string += doName;
		
		if (daName != null)
			string += "." + daName;
		
		return string;
	}

	public String srcToString() {
		String string = "";

		if (iedName != null)
			string += iedName;
		
		if (srcLDInst != null)
			string += srcLDInst;
		
		string	+= "/";
		
		if (srcLNClass != null) {
		    
		    if (srcPrefix != null)
		        string += srcPrefix;
		    
			string += srcLNClass;
			if (srcLNInst == null)
				string += ".";
		}
		
		if (srcLNInst != null)
			string += srcLNInst + ".";
		
		if (srcCBName != null)
			string += srcCBName;
		
		return string;
	}
	
	
}
