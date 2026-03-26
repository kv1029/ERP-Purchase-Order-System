--
-- PostgreSQL database dump
--

\restrict 3bBjxWawoJRCauV37aW5CfachmiJSUoBYN0orncbfONT3akKr85ro5PaECcdM2B

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-03-26 21:32:26

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16405)
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name character varying,
    sku character varying,
    price double precision,
    stock integer
);


ALTER TABLE public.products OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16404)
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_id_seq OWNER TO postgres;

--
-- TOC entry 5032 (class 0 OID 0)
-- Dependencies: 221
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- TOC entry 224 (class 1259 OID 16432)
-- Name: purchase_orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.purchase_orders (
    id integer NOT NULL,
    vendor_id integer,
    total double precision,
    status character varying,
    owner_email character varying
);


ALTER TABLE public.purchase_orders OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16431)
-- Name: purchase_orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.purchase_orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.purchase_orders_id_seq OWNER TO postgres;

--
-- TOC entry 5033 (class 0 OID 0)
-- Dependencies: 223
-- Name: purchase_orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.purchase_orders_id_seq OWNED BY public.purchase_orders.id;


--
-- TOC entry 220 (class 1259 OID 16390)
-- Name: vendors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vendors (
    id integer NOT NULL,
    name character varying,
    contact character varying,
    rating double precision
);


ALTER TABLE public.vendors OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16389)
-- Name: vendors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vendors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vendors_id_seq OWNER TO postgres;

--
-- TOC entry 5034 (class 0 OID 0)
-- Dependencies: 219
-- Name: vendors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vendors_id_seq OWNED BY public.vendors.id;


--
-- TOC entry 4867 (class 2604 OID 16408)
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- TOC entry 4868 (class 2604 OID 16435)
-- Name: purchase_orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchase_orders ALTER COLUMN id SET DEFAULT nextval('public.purchase_orders_id_seq'::regclass);


--
-- TOC entry 4866 (class 2604 OID 16393)
-- Name: vendors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vendors ALTER COLUMN id SET DEFAULT nextval('public.vendors_id_seq'::regclass);


--
-- TOC entry 4874 (class 2606 OID 16413)
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- TOC entry 4878 (class 2606 OID 16440)
-- Name: purchase_orders purchase_orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchase_orders
    ADD CONSTRAINT purchase_orders_pkey PRIMARY KEY (id);


--
-- TOC entry 4871 (class 2606 OID 16402)
-- Name: vendors vendors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vendors
    ADD CONSTRAINT vendors_pkey PRIMARY KEY (id);


--
-- TOC entry 4872 (class 1259 OID 16414)
-- Name: ix_products_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_products_id ON public.products USING btree (id);


--
-- TOC entry 4875 (class 1259 OID 16447)
-- Name: ix_purchase_orders_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_purchase_orders_id ON public.purchase_orders USING btree (id);


--
-- TOC entry 4876 (class 1259 OID 16446)
-- Name: ix_purchase_orders_owner_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_purchase_orders_owner_email ON public.purchase_orders USING btree (owner_email);


--
-- TOC entry 4869 (class 1259 OID 16403)
-- Name: ix_vendors_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_vendors_id ON public.vendors USING btree (id);


--
-- TOC entry 4879 (class 2606 OID 16441)
-- Name: purchase_orders purchase_orders_vendor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchase_orders
    ADD CONSTRAINT purchase_orders_vendor_id_fkey FOREIGN KEY (vendor_id) REFERENCES public.vendors(id);


-- Completed on 2026-03-26 21:32:26

--
-- PostgreSQL database dump complete
--

\unrestrict 3bBjxWawoJRCauV37aW5CfachmiJSUoBYN0orncbfONT3akKr85ro5PaECcdM2B

