import { Placeholder } from "@angular/compiler/src/i18n/i18n_ast";

export interface IHospital{
    name: string,
    type: string, 
    description: string,
    place: string,
    address: string
}

export interface IDoctor{
    name: string,
    mobile: string,
    address: string
}

export interface IPatient{
    name: string,
    mobile: string,
    address: string
}

export interface IMedicine{
    name: string,
    company: string,
    cost: number,
    type: string,
    description: string
}

export interface IAppointment{
    type: string,
    description: string,
    patient: IPatient,
    doctor: IDoctor
}