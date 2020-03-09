from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Vehicle(BaseModel):
    lotNumberStr: str
    ln: int
    mkn: str
    lm: str
    lcy: int
    fv: str
    la: float
    rc: float
    orr: float
    egn: Optional[str]
    cy: Optional[str]
    ld: str
    yn: Optional[str]
    cuc: str
    tz: Optional[str]
    at: str
    aan: int
    hb: float
    ss: int
    bndc: str
    bnp: float
    sbf: bool
    dd: str
    tims: Optional[str]
    lic: List[str] = []
    gr: str
    dtc: str
    ynumb: int
    phynumb: int
    bf: bool
    ymin: int
    offFlg: Optional[bool]
    htsmn: str
    tmtp: Optional[str]
    myb: str
    lmc: str
    lcc: Optional[str]
    sdd: Optional[str]
    lcd: Optional[str]
    ft: Optional[str]
    hk: str
    drv: Optional[str]
    ess: str
    showSeller: bool
    sstpflg: bool
    syn: Optional[str]
    ifs: bool
    pbf: bool
    crg: float
    brand: str
    hegn: str
